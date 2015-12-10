---
title: 总结一下Django利用Webhook来更新文章
tag:
    - Django
    - 博客搭建
author: disoul
date: 2015-06-28 13:00
---
主要思路是我在自己的电脑上写博，博文（在/blog/articles）push上去之后  
服务器那边可以自动pull并且执行add_article.py（通过比对articles文件夹类文件修改时间和最近保存的时间戳进行更新）

为了实现这个想法，主要使用的有

* simplyjson（处理github端的json文件）
* celery+redis （任务队列，处理我的pull和更新文章）
* subprocess (python创建自进程执行命令行)

其实也就这么简单，我自己都不知到我为啥弄好久，我是鶸比  
@@
###Simplejson
开始用Django自带的POST方法获取post发现不行，查阅一下才发现正规做法是先获取请求的源字符串再通过simplejson解析成json字典

```python
pip install simplejson

import simplejson
...
    post = simplejson.loads(request.body) #原来djangobook上的raw_post_data方法好像已经被新版本的body方法取代
...
```

###Celery+redis
开始气体和我说这个东西的时候觉得高大上，实际操作起来并不难  
因为使用django所以直接用django-celery这个包了  

```shell
pip install django-celery
pip install redis
sudo apt-get install redis-server
redis-server
```

其中使用redis作为Celery的Broker（具体见celery官网教程，如果是开发环境的话还可以用django自己的database作为broker）  
之后修改settings.py

```python
import djcelery

djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/0'
#这里还可以定义BACKEND用来储存celery返回的结果

INSTALLED_APPS = (
    ...
	'djcelery',
    ...
)
```

之后更新一波数据库，因为我django是1.8，所以执行

```shell
python manage.py migrate
```

现在就可以在django里注册我们的task了  
在app目录下创建tasks.py

```python
from celery import task

@task
def test_task():
    do_something
	return 1

```

之后在view里收到github的请求时就调用这个task  
最后启动worker  
python manage.py celery worker --loglevel=info
当收到请求时命令行下会输出1

###Subprocess
这些网上教程蛮多。。懒得打了
使用subprocess.Popen接受2种命令参数（字符串和列表）
官网上不建议使用字符串  
所以使用shlex.split()的方法把命令字符串变成列表传进去

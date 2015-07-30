我的blog搭建历程(2)
博客搭建
# 第一次部署
借了一波钱之后买了一年的阿里ECS，服务器是ubuntu的  
折腾备案等了半个月..  
基本配置完后就把博客pull进来了  
部署采用的方案是`uwsgi`和`nginx`    
因为有了不少之前学习的经验，所以直接找<a href="https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html">文档</a>也就顺利完成了（然而过程并不顺利...  
大概也就这个现在这个样子了...
@@
# 配置github的Webhook
这个在前几篇博客也提到了，想法是直接远程push服务器端自动pull  
然后气体有推荐我可以去借此机会学一学celery，于是遍有了那篇博文的折腾
<a href="http://disoul.me/blog/article/%E6%80%BB%E7%BB%93%E4%B8%80%E4%B8%8BDjango%E5%88%A9%E7%94%A8Webhook%E6%9D%A5%E6%9B%B4%E6%96%B0%E6%96%87%E7%AB%A0/">Webhook过程</a>  
基本实现了想要的样子，然而实话实说还是有点bug..  

# 之后的路
现在也就有个基本的样子，以后的话希望可以做出一个移动端适配的站点  
而且因为开始写这个项目的时候刚刚接触web，所以很多地方写的不好，以后也要重写  
总之web水太深，路还很长...

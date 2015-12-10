---
title: 使用Django的Paginator实现页面分页效果
tag:
    - Django
    - 博客搭建
author: disoul
date: 2015-06-23 23:00
---
给博客主页折腾了一个分页效果，简单看了下Paginator，不得不说Django官方文档真的很齐全  

##EXAMPLE
通过``from django.core.paginator import Paginator``引入Paginator，通过Paginator创建的对象拥有很多对分页效果实现有用的方法，具体见下面示例代码

```python
>>> from django.core.paginator import Paginator
>>> objects = ['john', 'paul', 'george', 'ringo']
>>> p = Paginator(objects, 2)

>>> p.count
4
>>> p.num_pages
2
>>> p.page_range
[1, 2]

>>> page1 = p.page(1)
>>> page1
<Page 1 of 2>
>>> page1.object_list
['john', 'paul']

>>> page2 = p.page(2)
>>> page2.object_list
['george', 'ringo']
>>> page2.has_next()
False
>>> page2.has_previous()
True
>>> page2.has_other_pages()
True
```
@@

```python
>>> page2.next_page_number()
Traceback (most recent call last):
...
EmptyPage: That page contains no results
>>> page2.previous_page_number()
1
>>> page2.start_index() # The 1-based index of the first item on this page
3
>>> page2.end_index() # The 1-based index of the last item on this page
4

>>> p.page(0)
Traceback (most recent call last):
...
EmptyPage: That page number is less than 1
>>> p.page(3)
Traceback (most recent call last):
...
EmptyPage: That page contains no results

```

只要对象拥有 ``count()`` 或者 ``__len__()`` 方法，那么就可以可以通过Paginator创建相应的Paginator对象  
例如Django里的QuerySet或者一个基础的列表  

##在view.py里使用Pagintor

```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"contacts": contacts})
```

这里是通过get请求来获取页面，也可以做url解析将页面当参数传进view    
通过上面示例的方法和异常，非常简单的就实现了传递相应页面的对象  
接下来只要在模板里做相应的修改，渲染这些对象就可以实现了  

##制作一个页面跳转链接

下面是官网给出的示例，通过{% if %}和Paginator的判断方法实现对不同页面发送get请求

```html
<div class="pagination">
    <span class="step-links">
        {% if contacts.has_previous %}
            <a href="?page={{ contacts.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ contacts.number }} of {{ contacts.paginator.num_pages }}.
        </span>

        {% if contacts.has_next %}
            <a href="?page={{ contacts.next_page_number }}">next</a>
        {% endif %}
    </span>
</div>
```

之后修改css完成页面跳转链接
至此简单实现了分页效果，也可以通过表单发送get实现跳页，不过现在做好像没啥用...(:3..

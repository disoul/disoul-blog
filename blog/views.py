from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import ArticleTags,Article

def home(request):
    homepage = get_template('home.html')
    tag_objs = ArticleTags.objects.all()
    article_objs = Paginator(Article.objects.all(),2)

    pagenum = request.GET.get('page')
    try:
        contacts = article_objs.page(pagenum)
    except PageNotAnInteger:
        contacts = article_objs.page(1)
    except EmptyPage:
        contacts = article_objs.page(paginator.num_pages)

    context = Context({
              'tags':tag_objs,
              'articles':contacts,
        })
    return HttpResponse(homepage.render(context))


def tag(request,tag_get):
    tagpage = get_template('tag.html')
    try:
        tag_obj = ArticleTags.objects.get(tag_name=tag_get)
    except ArticleTags.DoesNotExist:
        raise Http404()
    else:
        article_objs = tag_obj.article_set.all()
    context = Context({'articles':article_objs,
                       'tagname':tag_obj.tag_name,
        })
    return HttpResponse(tagpage.render(context))


def article(request,article_get):
    articlepage = get_template('article.html')
    try:
        article_obj = Article.objects.get(title = article_get)
    except Article.DoesNotExist:
        raise Http404()
    else:
        context = Context({'article':article_obj,})
    return HttpResponse(articlepage.render(context))


def aboutme(request):
    aboutmepage = get_template('aboutme.html')
    return HttpResponse(aboutmepage.render(Context({})))

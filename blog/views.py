from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from blog.models import ArticleTags,Article
import markdown2

def home(request):
    homepage = get_template('home.html')
    tag_objs = ArticleTags.objects.all()
    article_objs = Article.objects.all()
    for article_obj in article_objs:
        article_obj.content = MarkdownParse(article_obj.content)
    context = Context({
              'tags':tag_objs,
              'articles':article_objs,
        })
    return HttpResponse(homepage.render(context))

def MarkdownParse(content):
    return markdown2.markdown(content)

from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from blog.models import ArticleTags

def home(request):
    homepage = get_template('home.html')
    context = Context({
              'tags':ArticleTags.objects.all()
        })
    return HttpResponse(homepage.render(context))

from django.conf.urls import patterns,include,url
from blog.views import home

urlpatterns = patterns('',
              url(r'^$',home),
)

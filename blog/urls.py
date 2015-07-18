from django.conf.urls import include,url
from blog.webhook import updatehook
from blog.views import *

urlpatterns = [url(r'^$',home),
               url(r'^tag/(.*)/$',tag),
               url(r'^article/(.*)/$',article),
               url(r'^aboutme/$',aboutme),
               url(r'^webhook/$',updatehook),
              ]

from django.conf.urls import include,url
from blog.views import home

urlpatterns = [url(r'^$',home),
]

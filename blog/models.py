from django.db import models
from django.contrib import admin

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(ArticleTags)
    content = models.TextField()
    date = models.DateTimeField()


class BlogTitle(models.Model):
    icon = models.ImageField()
    text = models.CharField(max_length=100)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','tag','date')
    list_filter = ('date',)

admin.site.register(Article,ArticleAdmin)

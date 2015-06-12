from django.db import models
from django.contrib import admin

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_color = models.CharField(max_length=10)


class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(ArticleTags)
    content = models.TextField()
    date = models.DateTimeField()
    class Meta():
        ordering = ['-date']


class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date',)
    list_filter = ('date',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleTags,TagsAdmin)

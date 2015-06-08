from django.db import models
from django.contrib import admin

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_color = models.CharField(max_length=10)


class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(ArticleTags)
    content = models.TextField()
    date = models.DateTimeField()
    class Meta():
        ordering = ['-date']


class BlogTheme(models.Model):
    theme_name = models.CharField(max_length=100)
    icon = models.ImageField()
    title_text = models.CharField(max_length=100)
    title_img = models.ImageField()
    body_img = models.ImageField()


class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','tag','date',)
    list_filter = ('date',)


class BlogThemeAdmin(admin.ModelAdmin):
    list_display = ('theme_name',)



admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleTags,TagsAdmin)
admin.site.register(BlogTheme,BlogThemeAdmin)

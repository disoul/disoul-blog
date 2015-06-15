from django.contrib import admin
from blog.models import *

class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date',)
    list_filter = ('date',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleTags,TagsAdmin)

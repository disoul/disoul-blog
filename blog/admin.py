from django.contrib import admin
from blog.models import *

class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date',)
    list_filter = ('date',)


class updateAdmin(admin.ModelAdmin):
    list_display = ('update_type',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleTags,TagsAdmin)
admin.site.register(update_timetuple,updateAdmin)

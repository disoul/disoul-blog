from django.db import models

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(ArticleTags)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    preview_line = models.IntegerField()
    class Meta():
        ordering = ['-date']


class update_timetuple(models.Model):
    time = models.IntegerField()
    update_type = models.CharField(max_length=100)

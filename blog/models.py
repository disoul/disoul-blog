from django.db import models

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(ArticleTags)
    content = models.TextField()
    time = models.DateTimeField()


class BlogTitle(models.Model):
    icon = models.ImageField()
    text = models.CharField(max_length=100)

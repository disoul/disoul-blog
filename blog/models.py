from django.db import models

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(ArticleTags)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    class Meta():
        ordering = ['-date']

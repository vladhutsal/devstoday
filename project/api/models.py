from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    link = models.CharField(max_length=100, blank=True)
    author_name = models.CharField(max_length=50, blank=False)
    upvotes = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now=False, auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=500, blank=False)
    creation_date = models.DateField(auto_now=False, auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

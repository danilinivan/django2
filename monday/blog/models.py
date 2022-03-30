from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    thumb = models.ImageField(blank=True, default='image.jpeg')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='article_likes')
    dislikes = models.ManyToManyField(User, related_name='article_dislikes')

    def __str__(self):
        return self.title   

    def snippet(self):
        return f'{self.text[:20]}... read more' 

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()      

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.article} - {self.body[:50]}"         
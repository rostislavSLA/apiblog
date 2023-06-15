from django.db import models
from users.models import User


class Article(models.Model):
    ACCESS_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    access = models.CharField(max_length=20, choices=ACCESS_CHOICES, default='public')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering = ('-id',)
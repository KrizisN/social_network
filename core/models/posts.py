from django.db import models

from social_network.settings import AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(AUTH_USER_MODEL, related_name='liked_posts', blank=True)

from django.db import models

from core.models.posts import Post


def get_likes_by_date_range(date_from, date_to):
    return (
        Post.objects.filter(likes__date_joined__range=[date_from, date_to])
        .values('likes__date_joined__date')
        .annotate(likes_count=models.Count('likes'))
        .values('likes__date_joined__date', 'likes_count')
    )


def get_all_posts():
    return Post.objects.all()

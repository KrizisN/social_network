from rest_framework import serializers

from core.models.posts import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'created_at', 'likes')

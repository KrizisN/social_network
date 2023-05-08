from typing import Callable

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.serializers.posts import PostSerializer
from core.manager import posts as posts_manager


class BasePostAction(generics.GenericAPIView):
    queryset = posts_manager.get_all_posts()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    action: Callable = None

    def post(self, *args, **kwargs):
        post = self.get_object()
        self.action(post)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCreateView(generics.CreateAPIView):
    queryset = posts_manager.get_all_posts()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeView(BasePostAction):
    def like_action(self, post):
        post.likes.add(self.request.user)

    action = like_action


class PostUnlikeView(BasePostAction):
    def unlike_action(self, post):
        post.likes.remove(self.request.user)

    action = unlike_action

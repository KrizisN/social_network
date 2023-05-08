from django.urls import path
from .api.posts import PostCreateView, PostLikeView, PostUnlikeView
from .api.analytics import analytics
from .api.user import user_activity
from .api.auth import UserSignUpView, UserLoginView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('posts/<int:pk>/unlike/', PostUnlikeView.as_view(), name='post_unlike'),
    path('analytics/', analytics, name='analytics'),
    path('activity/', user_activity, name='user_activity'),
]

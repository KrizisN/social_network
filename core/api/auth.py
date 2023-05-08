from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers.auth import UserSerializer
from core.serializers.token import CustomTokenObtainPairSerializer
from users import manager as user_manager


class UserSignUpView(generics.CreateAPIView):
    queryset = user_manager.get_all_users()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)

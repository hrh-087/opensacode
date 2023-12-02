# coding:utf-8

from users.serializers.user_serializer import UserProfileSerializer, UserAddSerializer
from users.models import UserProfile

from utils.viewsets import CustomModelViewSet


class UserListViewSet(CustomModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserAddViewSet(CustomModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserAddSerializer

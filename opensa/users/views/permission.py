# coding:utf-8

from users.models import PermissionList
from users.serializers.permission_serializer import PermissionSerializer
from utils.viewsets import CustomModelViewSet

class PermissionViewSet(CustomModelViewSet):
    queryset = PermissionList.objects.all()
    serializer_class = PermissionSerializer
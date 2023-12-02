# coding:utf-8


from users.serializers.role_serializer import RoleSerializer
from users.models import RoleList

from utils.viewsets import CustomModelViewSet


class RoleListViewSet(CustomModelViewSet):
    queryset = RoleList.objects.all()
    serializer_class = RoleSerializer

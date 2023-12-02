# coding:utf-8


from users.serializers.menu_serializer import MenuSerializer
from users.models import MenuList

from utils.viewsets import CustomModelViewSet


class MenuListViewSet(CustomModelViewSet):
    queryset = MenuList.objects.all()
    serializer_class = MenuSerializer


# def
# coding:utf-8

from rest_framework.serializers import ModelSerializer

from users.models import MenuList

class MenuSerializer(ModelSerializer):

    class Meta:
        model = MenuList
        fields = "__all__"
        read_only_fields = [
            'id'
        ]
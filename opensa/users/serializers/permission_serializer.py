# coding:utf-8

from rest_framework.serializers import ModelSerializer

from users.models import PermissionList

class PermissionSerializer(ModelSerializer):

    class Meta:
        model = PermissionList
        fields = "__all__"
        read_only_fields = [
            'id'
        ]
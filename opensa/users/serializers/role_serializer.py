# coding:utf-8


from rest_framework.serializers import ModelSerializer

from users.models import RoleList


class RoleSerializer(ModelSerializer):
    class Meta:
        model = RoleList
        fields = "__all__"
        read_only_fields = [
            'id'
        ]

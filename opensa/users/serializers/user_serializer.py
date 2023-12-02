# coding:utf-8

from rest_framework.serializers import ModelSerializer

from users.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'email',
            'username',
            'mobile',
            'is_active',
            'level',
            'department',
            'role',
            'is_superuser',
            'comment'
        ]
        read_only_fields = [
            'id',
            'email',
            'username',
        ]


class UserAddSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'email',
            'username',
            'mobile',
            'is_active',
            'level',
            'department',
            'role',
            'is_superuser',
            'comment',
            'password'
        ]
        read_only_fields = [
            'id'
        ]

        extra_kwargs = {
            'username': {
                'max_length': 20,
                'min_length': 5
            },
            'password': {
                'max_length': 20,
                'min_length': 5,
                'write_only': True

            }
        }

    def create(self, validated_data):
        print('validated_data:', validated_data)
        user = UserProfile.objects.create_user(**validated_data) if not validated_data[
            'is_superuser'] else UserProfile.objects.create_superuser(**validated_data)
        return user

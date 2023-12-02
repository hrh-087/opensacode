# coding utf-8

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from utils.json_response import ErrorResponse, DetailResponse


class UserLoginViewSet(APIView):
    permission_classes = []

    def post(self, request):

        if 'HTTP_X_FORWARDED_FOR' in self.request.META:
            ipaddr = self.request.META['HTTP_X_FORWARDED_FOR']
        else:
            ipaddr = self.request.META['REMOTE_ADDR']

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_active:
                return ErrorResponse(msg="账户已被禁用")

            token = Token.objects.get(user=user)

            return DetailResponse(data={"token": token.key}, msg="登录成功")
        else:
            return ErrorResponse(msg="账号或密码不正确")

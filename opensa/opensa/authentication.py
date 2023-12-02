# coding : utf-8
import json

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from django_redis import get_redis_connection

redis_coon = get_redis_connection()


# class CustomAuthentication(TokenAuthentication):
#     def authenticate(self, request):
#         user_token = request.META.get("HTTP_AUTHORIZATION").split()
#         print(user_token)
#         if not user_token:
#             raise AuthenticationFailed("身份认证信息未提供")
#             # return
#         user_info = redis_coon.get(user_token)
#         if not user_info:
#             raise AuthenticationFailed("认证信息不存在或已过期")
#             # return
#         return json.loads(user_info), None

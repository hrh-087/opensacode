# coding:utf-8

from django.urls import path
from users.views.user import *
from users.views.role import *
from users.views.login import *

app_name = "users"

urlpatterns = [
    path("login/", UserLoginViewSet.as_view()),
    # 用户操作
    path("userList/", UserListViewSet.as_view({'get': 'list'}), name='userList'),
    path("userAdd/", UserAddViewSet.as_view({'post': 'create'}), name='userAdd'),
    path("userUpdate/", UserListViewSet.as_view({'post': 'update'}), name='userUpdate'),
    path("userDestroy/", UserListViewSet.as_view({'post': 'destroy'}), name='userDestroy'),
    path("userRetrieve/", UserListViewSet.as_view({'get': 'retrieve'}), name='userRetrieve'),
    # 角色操作
    path("roleList/", RoleListView.as_view({'get': 'list'}), name='roleList'),
    path("roleAdd/", RoleListView.as_view({'post': 'create'}), name='roleAdd'),
    path("roleUpdate/", RoleListView.as_view({'post': 'update'}), name='roleUpdate'),
    path("roleDestroy/", RoleListView.as_view({'post': 'destroy'}), name='roleDestroy'),
    path("roleRetrieve/", RoleListView.as_view({'get': 'retrieve'}), name='roleRetrieve'),
    # 权限操作



]

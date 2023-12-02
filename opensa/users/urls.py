# coding:utf-8

from django.urls import path
from users.views.user import *
from users.views.role import *
from users.views.permission import *
from users.views.menu import *
from users.views.login import *

app_name = "users"

urlpatterns = [
    path("login/", UserLoginViewSet.as_view()),
    # 用户操作
    path("userList/", UserListViewSet.as_view({'get': 'list'}), name='userList'),
    path("userAdd/", UserAddViewSet.as_view({'post': 'create'}), name='userAdd'),
    path("userUpdate/", UserListViewSet.as_view({'post': 'update'}), name='userUpdate'),
    path("userDestroy/", UserListViewSet.as_view({'post': 'destroy'}), name='userDestroy'),
    path("userDetail/", UserListViewSet.as_view({'get': 'retrieve'}), name='userDetail'),
    # 角色操作
    path("roleList/", RoleListViewSet.as_view({'get': 'list'}), name='roleList'),
    path("roleAdd/", RoleListViewSet.as_view({'post': 'create'}), name='roleAdd'),
    path("roleUpdate/", RoleListViewSet.as_view({'post': 'update'}), name='roleUpdate'),
    path("roleDestroy/", RoleListViewSet.as_view({'post': 'destroy'}), name='roleDestroy'),
    path("roleDetail/", RoleListViewSet.as_view({'get': 'retrieve'}), name='roleDetail'),
    # 权限操作
    path("permissionList/", PermissionViewSet.as_view({'get': 'list'}), name='permissionList'),
    path("permissionAdd/", PermissionViewSet.as_view({'post': 'create'}), name='permissionAdd'),
    path("permissionUpdate/", PermissionViewSet.as_view({'post': 'update'}), name='permissionUpdate'),
    path("permissionDestroy/", PermissionViewSet.as_view({'post': 'destroy'}), name='permissionDestroy'),
    path("permissionDetail/", PermissionViewSet.as_view({'get': 'retrieve'}), name='permissionDetail'),
    # 菜单操作
    path("menuList/", MenuListViewSet.as_view({'get': 'list'}), name='menuList'),
    path("menuAdd/", MenuListViewSet.as_view({'post': 'create'}), name='menuAdd'),
    path("menuUpdate/", MenuListViewSet.as_view({'post': 'update'}), name='menuUpdate'),
    path("menuDestroy/", MenuListViewSet.as_view({'post': 'destroy'}), name='menuDestroy'),
    path("menuDetail/", MenuListViewSet.as_view({'get': 'retrieve'}), name='menuDetail'),

]

# coding :utf-8


from rest_framework.permissions import BasePermission
from rest_framework.request import HttpRequest


class CustomPermissions(BasePermission):
    """
    自定义全局权限
    """

    def has_permission(self, request, view):
        # print(request.path)
        # print(request.resolver_match.url_name)
        # print(request.path_info)
        # print(isinstance(request, HttpRequest))
        # if isinstance(request.user, AnonymousUser):
        #     return False
        # if request.method == "GET":
        #     action = request.query_params.get("action")
        # else:
        #     action = request.data.get("action")
        # return request.path.rstrip("/").split("/")[-1] in request.user["accessArr"].keys() or action in request.user[
        #     "accessArr"].keys()
        return super(CustomPermissions, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return super(CustomPermissions, self).has_object_permission(request, view, obj)

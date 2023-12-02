# coding:utf-8

from rest_framework.viewsets import ModelViewSet
from utils.json_response import *


class CustomModelViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):

        return super(CustomModelViewSet, self).create(request)

    def update(self, request, *args, **kwargs):

        increment_id = request.data.get("id")
        instance = self.get_instance(increment_id)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return DetailResponse(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        increment_id = request.data.get("id")
        instance = self.get_instance(increment_id)
        serializer = self.get_serializer(instance)
        return DetailResponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        increment_id = request.data.get("id")

        for i in str(increment_id).split(","):
            instance = self.get_instance(i)
            self.perform_destroy(instance)

        return DetailResponse({})

    def get_instance(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except self.queryset.model.DoesNotExist:
            return ErrorResponse({}, msg="请求的资源不存在")

# coding :utf-8
import traceback
import logging

from rest_framework.exceptions import NotFound, AuthenticationFailed, PermissionDenied, NotAuthenticated,MethodNotAllowed

from rest_framework import serializers
from utils.json_response import ErrorResponse
from django.db import IntegrityError


def CustomExceptionHandler(ex, context):
    """
    统一异常拦截处理
    目的:(1)取消所有的500异常响应,统一响应为标准错误返回
        (2)准确显示错误信息
    :param ex:
    :param context:
    :return:
    """
    logger = logging.getLogger("err")
    logger.error(traceback.format_exc())

    if isinstance(ex, NotFound):
        return ErrorResponse(msg="页面未找到")

    elif isinstance(ex, MethodNotAllowed):
        return ErrorResponse(msg="请求方法不允许")

    elif isinstance(ex, (
            NotAuthenticated, AuthenticationFailed, CustomError,
            IntegrityError)):
        return ErrorResponse(msg=str(ex), status=ex.status_code)

    elif isinstance(ex, serializers.ValidationError):
        return ErrorResponse(msg=ex.__dict__["detail"])

    elif isinstance(ex, PermissionDenied):
        return ErrorResponse(msg="无{}操作权限，请联系管理员添加".format(
            context["view"].request.user["accessArr"].get(
                context["view"].request.path.rstrip("/").split("/")[-1], "")))

    else:
        return ErrorResponse(msg="未知错误,请联系管理员查看")


class CustomError(ValueError):
    pass

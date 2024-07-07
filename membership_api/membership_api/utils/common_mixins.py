"""
@Author: star320129
@Email: star_320129@sina.com
@FileName: common_mixins.py
@DoteTime: 2024/7/7 21:48
"""

from .common_response import CommonResponse
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class CommonListMixins(ListModelMixin):
    """
    查询所有
    """
    def list(self, request, *args, **kwargs):

        res = super().list(request, *args, **kwargs)

        return CommonResponse(message="查询所有成功!", data=res.data)


class CommonCreateMixins(CreateModelMixin):
    """
    创建
    """
    def create(self, request, *args, **kwargs):

        res = super().create(request, *args, **kwargs)

        return CommonResponse(message="新增成功!", data=res.data)


class CommonRetrieveMixins(RetrieveModelMixin):
    """
    查询单条
    """
    def retrieve(self, request, *args, **kwargs):

        res = super().retrieve(request, *args, **kwargs)

        return CommonResponse(message="查询成功!", data=res.data)


class CommonDestroyMixins(DestroyModelMixin):
    """
    删除
    """
    def destroy(self, request, *args, **kwargs):

        super().destroy(request, *args, **kwargs)

        return CommonResponse(message="删除成功!")

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class CommonUpdateMixins(UpdateModelMixin):
    """
    更新
    """
    def update(self, request, *args, **kwargs):

        res = super().update(request, *args, **kwargs)

        return CommonResponse(message="更新成功!", data=res.data)

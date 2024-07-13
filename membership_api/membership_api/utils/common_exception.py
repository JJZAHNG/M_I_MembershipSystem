# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/28 20:34
@Auth ： flq
@File ：common_exception.py
@IDE ：PyCharm
"""
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
import loguru


def exception_handler(exc, context):
    request = context['request']
    view = context['view']
    ip = request.META.get('REMOTE_ADDR')
    path = request.get_full_path()
    method = request.method
    try:
        user_id = request.user.id
    except:
        user_id = '匿名用户'
    loguru.logger.error(f"{str(exc)} {user_id} {ip} {path} {method} {exc} {view}")
    res = drf_exception_handler(exc, context)
    if res:
        if isinstance(res.data, dict):
            print(res.data)
            err = res.data.get('detail') or res.data.get('non_field_errors') or '系统错误'
        elif isinstance(res.data, list):
            err = res.data[0]
        else:
            err = '服务器异常'
        response = Response({'code': 400, 'msg': err})
    else:

        err = f'{str(exc)}'
        code = 500
        response = Response({'code': code, 'msg': err})
    return response

###############################################################################
# from rest_framework.exceptions import AuthenticationFailed, ValidationError
# from django.http import Http404
# from django.db.utils import IntegrityError
# code_dict = {
#     # 认证失败
#     AuthenticationFailed: 401,
#     # 字段校验失败
#     ValidationError: 402,
#     # 字段值重复
#     IntegrityError: 403,
#     # 页面未找到
#     Http404: 404
# }
#
#
# def exception_handle(exc, context):
#     request = context.get('request')
#     view = context.get('view')
#     ip = request.META.get('REMOTE_ADDR')
#     user_id = request.user.id if request.user else '【匿名用户】'
#     logger.error(
#         f'{view.get_view_name()}|{str(exc)}|ip地址为：{ip}|用户{user_id}')
#     # 先执行drf自带的异常捕获
#     res = drf_exception_handler(exc, context)
#     if res:
#         # drf的异常 data=['错误1',错误2]    data={detail:'sss'}
#         if isinstance(res.data, dict):
#             # err = ''.join([f'【{key}|{value[0]}】-' for key, value in res.data.items()])
#             err = list(res.data.values())[0] or '未知错误'
#         elif isinstance(res.data, list):
#             err = res.data[0]
#         else:
#             err = 'drf服务异常，请稍后再尝试'
#         code = code_dict.get(exc.__class__) or 999
#         response = APIResponse(code, msg=err)
#     else:
#         # 非drf异常，更细力度的区分异常
#         code = code_dict.get(exc.__class__) or 989
#         response = APIResponse(code, msg=str(exc))
#     return response
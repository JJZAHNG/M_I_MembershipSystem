# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/28 20:34
@Auth ： flq
@File ：common_exception.py
@IDE ：PyCharm
"""
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
import logging


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
    logging.error(f"{str(exc)} {user_id} {ip} {path} {method} {exc} {view}")
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

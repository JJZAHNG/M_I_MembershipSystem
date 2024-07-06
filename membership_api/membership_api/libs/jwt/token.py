# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/29 20:04
@Auth ： flq
@File ：token.py
@IDE ：PyCharm
"""
import jwt
from datetime import datetime
from .setting_manager import jwt_settings


class Token:
    @classmethod
    def get_token(cls, user):
        rolo_list = []
        for i in user.role.all():
            rolo_list.append(i.id)
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + jwt_settings.ACCESS_TOKEN_LIFETIME,  # token的过期时间的时间戳
            'iat': datetime.utcnow()
        }
        jwt_encode = jwt.encode(payload, jwt_settings.SINGING_KEY, algorithm=jwt_settings.ALGORITHM)
        return jwt_encode

    @classmethod
    def get_payload(cls, token):
        options = {'verify_exp': True}
        payload = jwt.decode(token, jwt_settings.SINGING_KEY, algorithms=jwt_settings.ALGORITHM, options=options)
        return payload

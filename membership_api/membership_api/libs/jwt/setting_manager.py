# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/29 20:04
@Auth ： flq
@File ：setting_manager.py
@IDE ：PyCharm
"""
from django.conf import settings
from . import settings as DEFAULTS

USER_SETTINGS = getattr(settings, 'JWT_SETTINGS', {})


class JWTSettings:
    def __init__(self):
        for setting in dir(DEFAULTS):
            if setting.isupper():
                setattr(self, setting, getattr(DEFAULTS, setting))
        for setting in USER_SETTINGS.keys():
            if setting.isupper():
                setattr(self, setting, USER_SETTINGS[setting])


jwt_settings = JWTSettings()

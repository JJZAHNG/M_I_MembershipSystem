# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/29 20:04
@Auth ： flq
@File ：settings.py
@IDE ：PyCharm
"""
from datetime import timedelta
from django.conf import settings

ACCESS_TOKEN_LIFETIME = timedelta(minutes=5)
ALGORITHM = "HS256"
SINGING_KEY = settings.SECRET_KEY

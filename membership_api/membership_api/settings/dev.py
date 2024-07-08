import os
import sys
from pathlib import Path

# membership_api/
BASE_DIR = Path(__file__).resolve().parent.parent
# membership_api/membership_apiresolve
sys.path.append(os.path.join(BASE_DIR))
# membership_api/membership_api/apps
sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'django-insecure-gqj6t8bl@no8sb2&ftm^kgs7-vzoi%m)s3@n^^-ey7t@g)-m&f'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'rest_framework',
    'user',
    'course',
    'mall',
    'member',
    'system',
]

MIDDLEWARE = [

]

ROOT_URLCONF = 'membership_api.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates']
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'membership_api.wsgi.application'

# ================================================= #
# ************** mysql数据库 配置  ************** #
# ================================================= #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_db',
        'USER': 'mi',
        'PASSWORD': 'Mi123?',
        'HOST': 'rm-bp16n7owypkw5g322do.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# media 文件目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ================================================= #
# ******************* 跨域 配置  ******************* #
# ================================================= #
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'Token',
    'host',
    'referer',
)

# ================================================= #
# ******************* 日志 配置  ******************* #
# ================================================= #
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'ERROR',
            'class': 'utils.common_logger.InterceptTimedRotatingFileHandler',
            # 日志位置,日志文件名
            'filename': os.path.join(BASE_DIR, "logs", "mi.log"),
            # 日志文件的最大值,这里我们设置300M
            # 'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            # 'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

# LOGGING_CONFIG = "utils.common_logger.simple_log_injector"

# ================================================= #
# ******************* redis 配置  ******************* #
# ================================================= #
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": '',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "123",
        }
    }
}

# ================================================= #
# ************ REST_FRAMEWORK 配置  ************* #
# ================================================= #
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.common_exception.exception_handler',
    "UNAUTHENTICATED_USER": None,
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'permission.common_permission.UserPermission'
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'permission.authenticate.LoginAuthentication'
    # ],
    # 频率类
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'user.throttle.CommonThrottle'
    # ],
}

# ================================================= #
# ************ Celery redis 配置  ***************** #
# ================================================= #
# Broker配置，使用Redis作为消息中间件
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
# BACKEND配置，使用redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json'
# 任务结果过期时间，秒
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 时区配置
CELERY_TIMEZONE = 'Asia/Shanghai'

# from datetime import timedelta
#
# CELERY_BEAT_SCHEDULE = {
#     'mysql_backup': {
#         'task': 'system.tasks.mysql_backup',
#         'schedule': timedelta(seconds=5),
#         'args': ()
#     },
# }

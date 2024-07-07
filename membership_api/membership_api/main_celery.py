import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffy_api.settings.dev")

app = Celery('luffy_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

import os
from celery import Celery, platforms

from worker import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobs_web_django.settings')

celery_app = Celery('Jobs_web_django')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True  #加上这一行


def call_by_worker(func):
    task = celery_app.task(func)
    return task.delay

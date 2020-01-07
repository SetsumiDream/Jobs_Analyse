import os
from celery import Celery

from worker import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobs_web_django.settings')

celery_app = Celery('Jobs_web_django')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()


def call_by_worker(func):
    task = celery_app.task(func)
    return task.delay

from __future__ import absolute_import
import os

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mwach.settings')

app = Celery()

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, name="Debugggg")
def debug_task(self):
    logger.info("XYZ")
    logger.info('Request: {0!r}'.format(self.request))
    print('Request: {0!r}'.format(self.request))
    print("ABC")

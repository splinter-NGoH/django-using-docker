import os

from celery import Celery


from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_api.settings.local")

app = Celery("auth_api")

app.config_from_object("django.conf:settings", namespace="CELERY")
   
   
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
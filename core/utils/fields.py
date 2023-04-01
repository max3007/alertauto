from django.conf import settings
from django.db import models

from .storages import PrivateRootS3Boto3Storage


class PrivateFileField(models.FileField):
    def __init__(self, verbose_name=None, name=None, upload_to='', storage=None, **kwargs):
        storage = None
        if hasattr(settings, 'AWS_PRIVATE_MEDIA_LOCATION'):
            storage = PrivateRootS3Boto3Storage()
        super().__init__(verbose_name, name, upload_to, storage, **kwargs)

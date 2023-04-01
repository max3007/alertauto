import time
import boto3
import logging
from storages.backends.s3boto3 import S3Boto3Storage
from config.settings import base as settings


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False
    default_acl = "public-read"


class PrivateRootS3Boto3Storage(S3Boto3Storage):
    bucket_name = settings.AWS_PRIVATE_BUCKET_NAME
    location = "private"
    file_overwrite = False
    querystring_auth = True
    querystring_expire = 60


s3 = boto3.client('s3')
s3_bucket_name = 'logs'


class S3Handler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        filename = 'django-{}.log'.format(time.strftime('%d-%m-%Y_%H-%M-%S'))
        s3.put_object(Bucket=s3_bucket_name, Key=filename, Body=log_entry)

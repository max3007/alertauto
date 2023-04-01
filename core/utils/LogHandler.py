from django.conf import settings
import logging
import boto3
import time
import os

if settings.DEBUG == False:
    s3 = boto3.client('s3')
    s3_bucket_name = 'my-bucket-name'

    class S3Handler(logging.Handler):
        def emit(self, record):
            log_entry = self.format(record)
            filename = 'django-{}.log'.format(time.strftime('%Y-%m-%d_%H-%M-%S'))
            s3.put_object(Bucket=s3_bucket_name, Key=filename, Body=log_entry)

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            's3': {
                'level': 'INFO',
                'class': 'myapp.logging.S3Handler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'myapp': {
                'handlers': ['s3'],
                'level': 'INFO',
            },
        },
    }

else:
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }

logging.config.dictConfig(logging_config)

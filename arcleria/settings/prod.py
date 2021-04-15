from .common import *
import os

import pymysql
pymysql.version_info = (1, 4, 2, "final", 0)  # mysqlclient 버전 연동
pymysql.install_as_MySQLdb()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allow URL
ALLOWED_HOSTS = ['127.0.0.1', 'arcleria.com', 'www.arcleria.com']

# DB env
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'arcleria-3.ckqg3kjdybxm.ap-northeast-2.rds.amazonaws.com',
            'NAME': 'arcleria',
            'USER': 'arcleria',
            'PASSWORD': '2020dkzm!',
            'PORT': '3306',
        },
}

# Add app : django-storages
INSTALLED_APPS += ['storages']

# Change default storage
STATICFILES_STORAGE = 'arcleria.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'arcleria.storages.MediaS3Boto3Storage'

# S3 File management
AWS_ACCESS_KEY_ID = 'AKIA2FTSONLNRFY5MDDB'  # required
AWS_SECRET_ACCESS_KEY = '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'  # required
AWS_STORAGE_BUCKET_NAME = 'arcleria-s3'  # required
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-2')
AWS_S3_CUSTOM_DOMAIN = "arcleria-s3.s3.amazonaws.com"
AWS_DEFAULT_ACL = None
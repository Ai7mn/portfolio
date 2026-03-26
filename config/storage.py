import os
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import FileSystemStorage

class CustomFileSystemStorage(FileSystemStorage):
    pass

class MediaS3Storage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

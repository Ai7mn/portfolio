from django.conf import settings
from django.core.files.storage import DefaultStorage
from storages.backends.azure_storage import AzureStorage


class MediaAzureStorage(AzureStorage):
    account_name = 'devicesarena'
    account_key = settings.AZURE_SECRET_ACCESS_KEY
    azure_container = 'portfolio/media'
    expiration_secs = None

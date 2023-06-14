from django.core.files.storage import DefaultStorage


class NoCompressionStorage(DefaultStorage):
    def save(self, name, content, max_length=None):
        self._save(name, content)
        return name

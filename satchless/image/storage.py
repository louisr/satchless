import hashlib
import os.path

from django.core.files.storage import FileSystemStorage

class HashedStorage(FileSystemStorage):
    def save(self, name, content):
        if name is None:
            name = content.name

        hasher = hashlib.md5()
        for chunk in content.chunks():
            hasher.update(chunk)
        hash = hasher.hexdigest()

        directory, file_name = os.path.split(name)
        name = os.path.join(directory, 'by-md5', hash[:1], hash[1:2], hash, file_name)

        return super(HashedStorage, self).save(name, content)
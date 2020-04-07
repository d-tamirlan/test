from django.db import models
from uuid import uuid4


class Application(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    api_key = models.UUIDField('Ключ API', default=uuid4().hex, unique=True, db_index=True)

    def generate_api_key(self):
        self.api_key = uuid4().hex

    def __str__(self):
        return f'{self.name} | {self.api_key}'

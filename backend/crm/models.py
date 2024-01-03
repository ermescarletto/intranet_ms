
import hashlib
import pathlib
from django.db import models


class AreaAtuacao(models.Model):
    nome = models.CharField(max_length=60)
    
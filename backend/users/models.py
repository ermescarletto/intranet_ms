from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=255,verbose_name="Nome",null=True)
    last_name = models.CharField(max_length=255,verbose_name="Sobrenome",null=True)
    username = None
    email = models.EmailField(unique=True, verbose_name="E-mail")
    cpf = models.CharField(max_length=11,verbose_name="CPF")
    telefone = models.CharField(max_length=11,verbose_name="Telefone")
    data_nascimento = models.DateField(blank=True, null=True,verbose_name="Data de Nascimento")
    password_set = models.BooleanField(default=False,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf","data_nascimento","username"]
    EMAIL_FIELD = 'email'

    def to_dict_verbose(self,fields):
        data = {}
        for field in self._meta.fields:
                if field.name in fields:
                    verbose_name = field.verbose_name
                    value = getattr(self, field.attname)
                    data[verbose_name] = value
        return data

from django.db import models

# Create your models here.
import hashlib
import pathlib
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser


#CLASSE DE USUÁRIO PARA A INTRANET
class Unidade(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    
class Departamento(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

    

class Cargo(models.Model):
    descricao = models.CharField(max_length=255)
    dia_festivo = models.DateField(null=True)
    def __str__(self):
        return self.descricao

    
class PerfilColaborador(models.Model): 
    usuario = models.OneToOneField('users.User',on_delete=models.CASCADE)
    bio = models.TextField()
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    imagem = models.ImageField(null=True, blank=True)


class Banner(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to="upload/banners/imagens/",blank=True)
    ativo = models.BooleanField(default=False)
    criado_por = models.ForeignKey(PerfilColaborador, on_delete=models.CASCADE)

class Comunicados(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    data = models.DateField(auto_created=True,auto_now=True)
    criado_por = models.ForeignKey(PerfilColaborador, on_delete=models.CASCADE)
    expira = models.BooleanField(default=False)
    data_expira = models.DateField(null=True)
    anexo = models.FileField(upload_to="upload/comunicados/anexos/",blank=True)
    imagem = models.ImageField(upload_to="upload/comunicados/imagens/",blank=True)
    enviado = models.BooleanField(default=False)

class EnviosComunicados(models.Model):
    comunicado = models.ForeignKey(Comunicados,on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento)
    unidades = models.ManyToManyField(Unidade)
    enviado_em = models.DateField(auto_created=True,auto_now=True)

class MeusComunicados(models.Model):
    colaborador = models.ForeignKey(PerfilColaborador,on_delete=models.CASCADE)
    comunicado = models.ForeignKey(Comunicados,on_delete=models.CASCADE)
    lido = models.BooleanField(default=False)
    lido_em = models.DateField()

class CadastroPolitica(models.Model):
    codigo_politica = models.CharField(max_length=15)
    titulo_politica = models.CharField(max_length=255)
    texto_politica = models.TextField()

class AnexosCadastroPolitica(models.Model):
    politica = models.ForeignKey(CadastroPolitica, on_delete=models.CASCADE)
    anexo = models.FileField(upload_to='politicas/')
    comentario = models.CharField(max_length=255, null=True, blank=True)


class ProcedimentoPadrao(models.Model):
    politica = models.ForeignKey(CadastroPolitica, on_delete=models.CASCADE)
    titulo_procedimento = models.CharField(max_length=255)
    texto_procedimento = models.TextField()
    anexo = models.FileField(upload_to='politicas/pops/')


class DocumentosEmpresa(models.Model):
    unidade = models.ForeignKey(Unidade,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    validade = models.DateField()
    notifica_em = models.IntegerField()
    arquivo = models.FileField(upload_to='documentos/')
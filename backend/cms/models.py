from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class BannerCampanha(models.Model):
    titulo_campanha = models.CharField(max_length=255,verbose_name='Título')
    slogan_campanha = models.CharField(max_length=255,verbose_name='Texto')
    imagem_campanha = models.ImageField(upload_to='campanhas/')
    data_inicial = models.DateField()
    data_final = models.DateField()
    ativo = models.BooleanField()
    exibir_texto = models.BooleanField(default=False)


class CategoriaArtigo(models.Model):
    categoria = models.CharField(max_length=255)

class Artigo(models.Model):
    categoria = models.ForeignKey(CategoriaArtigo,on_delete=models.CASCADE)
    created_by = models.ForeignKey('users.User',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    texto = RichTextField()
    publicado = models.BooleanField(default=False)
    data_publicacao = models.DateField(auto_created=True,auto_now=True)





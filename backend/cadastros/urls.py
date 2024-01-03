from django.urls import path, include
from .views import *
app_name = 'cadastros'
urlpatterns = [
    path('api/cidades/', CidadeList.as_view(), name='cidade_list_create'),
    path('api/bairros/',BairroList.as_view(), name='bairro_list_create'),
    path('api/logradouros/', LogradouroList.as_view(),name='logradouro_list_create'),
    path('api/pessoas/',PessoaFisicaList.as_view(),name='pessoa_fisica_list_create'),
    
    
    ################# URLS CRUD TEMPLATE #############
    path('cidades/',CidadesListView.as_view(), name='list_cidades'),
   
   
   
   
    path('pessoas/',PessoasListView.as_view(), name='list_pessoas'),
    path('pessoas/create/',PessoaFisicaCreateView.as_view(), name='create_pessoas'),
    path('pessoas/edit/<int:pk>',PessoaFisicaCreateView.as_view(), name='edit_pessoas'),
    path('pessoas/remove/<int:pk>',PessoaFisicaCreateView.as_view(), name='remove_pessoas'),
    path('pessoas/detail/<int:pk>',PessoaFisicaCreateView.as_view(), name='detail_pessoas'),

]


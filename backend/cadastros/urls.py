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

    ################ URLS CADASTRO DE BAIRROS ###############
    path('bairros/',BairroListView.as_view(), name='list_bairros'),
    path('bairros/create',BairroCreateView.as_view(), name='create_bairro'),
    path('bairros/edit/<int:pk>',BairroEditView.as_view(), name='edit_bairro'),
    path('bairros/remove/<int:pk>',BairroDeleteView.as_view(), name='remove_bairro'),
    
    ################ URLS CADASTRO DE LOGRADOURO ###############

    path('logradouros/',LogradourosListView.as_view(), name='list_logradouros'),
    path('logradouros/create',LogradouroCreateView.as_view(), name='create_logradouro'),
    path('ajax/get-bairros/', BuscaBairroCidade.as_view(), name='get_bairros'),

   
    path('pessoas/',PessoasListView.as_view(), name='list_pessoas'),
    path('pessoas/create/',PessoaFisicaCreateView.as_view(), name='create_pessoas'),
    path('pessoas/edit/<int:pk>',PessoaFisicaCreateView.as_view(), name='edit_pessoas'),
    path('pessoas/remove/<int:pk>',PessoaFisicaCreateView.as_view(), name='remove_pessoas'),
    path('pessoas/detail/<int:pk>',PessoaFisicaCreateView.as_view(), name='detail_pessoas'),

]


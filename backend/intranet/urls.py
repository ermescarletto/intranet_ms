from django.urls import path, include
from .views import *
app_name = 'intranet'
urlpatterns = [
    path('api/unidades/', UnidadeListCreateAPIView.as_view(), name='unidade-list-create'),
    path('api/unidades/<int:pk>/', UnidadeDetailAPIView.as_view(), name='unidade-detail'),
    path('api/departamentos/', DepartamentoListCreateAPIView.as_view(), name='departamento-list-create'),
    path('api/departamentos/<int:pk>/', DepartamentoDetailAPIView.as_view(), name='departamento-detail'),
    path('api/cargos/', CargoListCreateAPIView.as_view(), name='cargo-list-create'),
    path('api/cargos/<int:pk>/', CargoDetailAPIView.as_view(), name='cargo-detail'),
    path('api/perfilcolaboradores/', PerfilColaboradorListCreateAPIView.as_view(), name='perfilcolaborador-list-create'),
    path('api/perfilcolaboradores/<int:pk>/', PerfilColaboradorDetailAPIView.as_view(), name='perfilcolaborador-detail'),
    path('api/comunicados/', ComunicadosListCreateAPIView.as_view(), name='comunicados-list-create'),
    path('api/comunicados/<int:pk>/', ComunicadosDetailAPIView.as_view(), name='comunicados-detail'),
    path('api/envioscomunicados/', EnviosComunicadosListCreateAPIView.as_view(), name='envioscomunicados-list-create'),
    path('api/envioscomunicados/<int:pk>/', EnviosComunicadosDetailAPIView.as_view(), name='envioscomunicados-detail'),
    path('api/meuscomunicados/', MeusComunicadosListCreateAPIView.as_view(), name='meuscomunicados-list-create'),
    path('api/meuscomunicados/<int:pk>/', MeusComunicadosDetailAPIView.as_view(), name='meuscomunicados-detail'),
    path('',EnterpriseHome.as_view(), name='enterprise_home'),

    ##### VIEWS DE CONFIGURAÇÃO ####
    ##### ECJ 22/11/2023 ###########
    ##### ##########################
    
    path('unidades/',UnidadesList.as_view(), name='create_unidade'),
    path('departamentos/',DepartamentosList.as_view(), name='create_departamento'),
    path('cargos/', CargosList.as_view(), name='create_cargo'),
    path('equipe/',EquipeListView.as_view(), name='equipe'),
    path('edit_perfil/<int:pk>',PerfilEdit.as_view(),name='perfil_edit'),
    path('create_perfil/<str:hashid>',PerfilCreateModalView.as_view(),name='perfil_create')

    
]

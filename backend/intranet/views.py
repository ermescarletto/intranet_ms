import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View, TemplateView
from rest_framework import generics
from .models import Unidade, Departamento, Cargo, PerfilColaborador, Comunicados, EnviosComunicados, MeusComunicados
from .serializers import UnidadeSerializer, DepartamentoSerializer, CargoSerializer, PerfilColaboradorSerializer, ComunicadosSerializer, EnviosComunicadosSerializer, MeusComunicadosSerializer
from cms import models as cms
from users import models as usr
class UnidadeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class UnidadeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class DepartamentoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class CargoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class CargoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class PerfilColaboradorListCreateAPIView(generics.ListCreateAPIView):
    queryset = PerfilColaborador.objects.all()
    serializer_class = PerfilColaboradorSerializer

class PerfilColaboradorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilColaborador.objects.all()
    serializer_class = PerfilColaboradorSerializer

class ComunicadosListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comunicados.objects.all()
    serializer_class = ComunicadosSerializer

class ComunicadosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunicados.objects.all()
    serializer_class = ComunicadosSerializer

class EnviosComunicadosListCreateAPIView(generics.ListCreateAPIView):
    queryset = EnviosComunicados.objects.all()
    serializer_class = EnviosComunicadosSerializer

class EnviosComunicadosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnviosComunicados.objects.all()
    serializer_class = EnviosComunicadosSerializer

class MeusComunicadosListCreateAPIView(generics.ListCreateAPIView):
    queryset = MeusComunicados.objects.all()
    serializer_class = MeusComunicadosSerializer

class MeusComunicadosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeusComunicados.objects.all()
    serializer_class = MeusComunicadosSerializer


########################################################################################################
######################## ENTERPRISE HOME ###############################################################
################################################ 2708 CZ ###############################################

from django.utils import timezone
from datetime import date

class EnterpriseHome(LoginRequiredMixin,TemplateView):
    context = {}
    template_name = 'home.html'
    current_month = timezone.now().month
    current_year = timezone.now().year
    def get_aniversariantes(self):
        aniversariantes = usr.User.objects.filter(
            data_nascimento__month=self.current_month
        )
        return aniversariantes
    
    def get(self, request, *args, **kwargs):
        self.context['imagens_campanha'] = cms.BannerCampanha.objects.filter(ativo=True, data_inicial__lte=datetime.date.today(), data_final__gte=datetime.date.today())
        self.context['aniversariantes'] = self.get_aniversariantes()
        print(self.context['aniversariantes'])
        return self.render_to_response(self.context)



#################################################################
########### VIEWS DAS CONFIGURAÇÕES #############################
#################################################################
#################################################################

class UnidadesList(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        unidades = Unidade.objects.all().order_by('id').values()
        context = {
            'unidades' : unidades,
            'page_title' : 'Cadastro de Unidades'
        }
        return render(request,"unidades/list_unidades.html", context=context)


class DepartamentosList(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        departamentos = Departamento.objects.all().order_by('id').values()
        context = {
            'departamentos' : departamentos,
            'page_title' : 'Cadastro de Departamentos'
        }
        return render(request,"departamentos/list_departamentos.html", context=context)


class CargosList(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        cargos = Cargo.objects.all().order_by('id').values()
        context = {
            'cargos' : cargos,
            'page_title' : 'Cadastro de Cargos'
        }
        return render(request,"cargos/list_cargos.html", context=context)






##################################################################
###################### VIEWS DA EQUIPE ###########################
############ AQUI A LÓGICA É SIMPLES, BUSCA TODOS ################
############ DEMONSTRA OS DADOS DO MODELO USER + PERFIL ##########
##################################################################
## 2708 #####"Essas palavras que escrevo me protegem #############  
###################### da completa loucura."#######$##############
################################################################## 



class EquipeListView(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        usuarios = usr.User.objects.all().order_by('id').values()
        context = {
            'usuarios' : usuarios,
            'page_title' : 'Visualizando Equipe'
        }
        return render(request,"equipe/list.html", context=context)


##################################################################################
#### AQUI FICA A VIEW DE EDIÇÃO DO PERFIL DO USUÁRIO #############################
##################################################################################

from .forms import PerfilUserForm, PerfilColaboradorForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView, BSModalUpdateView, BSModalDeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class PerfilCreateModalView(BSModalCreateView,SuccessMessageMixin,LoginRequiredMixin):
    login_url = '/user/login/'
    template_name = 'generic/create.html'
    form_class = PerfilColaboradorForm
    success_message = 'Perfil criado com sucesso.'
    success_url = reverse_lazy('users:user_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modal_title"] = 'Perfil de Usuário'
        context["hint"] = 'Vincule o usuário para que possa ter acesso às políticas.'

        return context
    
from django.forms.models import model_to_dict


class PerfilEdit(BSModalUpdateView, LoginRequiredMixin):
    login_url = '/user/login/'
    model = PerfilColaborador
    template_name = 'generic/edit.html'
    form_class = PerfilColaboradorForm
    success_message = 'Usuário editado com sucesso'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modal_title"] = 'Editar perfil'
        context["hint"] = '*Cuidado, você está editando um usuário do sistema.'

        return context


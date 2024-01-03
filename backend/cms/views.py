from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BannerCampanha
from django.contrib import messages
# Create your views here.

class BannerListView(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        campanhas = BannerCampanha.objects.all().order_by('id').values()
        context = {
            'campanhas' : campanhas,
            'page_title' : 'Cadastro de Campanhas'
        }
        return render(request,"campanha/list_campanha.html", context=context)


############################################################################################
######## VIEWS PARA O BS MODAL FORMS - ATIVA OS MODAIS DE ACORDO COM A AÇÃO DO CRUD ########
############################################################################################
#2708#:(####################################################################################

from django.urls import reverse_lazy
from .forms import BannerCampanhaModelForm
from .models import BannerCampanha
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView, BSModalUpdateView, BSModalDeleteView
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect

class BannerCampanhaCreateView(BSModalCreateView,LoginRequiredMixin):
    login_url = '/user/login/'
    template_name = 'campanha/create.html'
    form_class = BannerCampanhaModelForm
    success_message = 'Campanha criada com sucesso.'
    success_url = reverse_lazy('cms:banner_list')

class BannerCampanhaDetailView(BSModalReadView, LoginRequiredMixin):
    login_url = '/user/login/'
    template_name = 'campanha/detail.html'
    model = BannerCampanha

class BannerCampanhaEditView(BSModalUpdateView, LoginRequiredMixin):
    login_url = '/user/login/'
    model = BannerCampanha
    template_name = 'campanha/edit.html'
    form_class = BannerCampanhaModelForm
    success_message = 'Campanha editada com sucesso'
    success_url = reverse_lazy('cms:banner_list')

class BannerCampanhaDeleteView(BSModalDeleteView, LoginRequiredMixin):
    login_url = '/user/login/'
    model = BannerCampanha
    template_name = 'campanha/delete.html'
    success_message = 'Campanha removida com sucesso.'
    error_message = 'Não foi possível remover este banner.'
    success_url = reverse_lazy('cms:banner_list')
    error_url = reverse_lazy('cms:banner_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(request, "Não foi possível excluir o registro.")
        finally:
            return HttpResponseRedirect(success_url)

############################################################################################



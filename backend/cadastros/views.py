from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .forms import *
# Create your views here.


class CidadeList(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class CidadeCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class BairroList(generics.ListCreateAPIView):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer

class BairroCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer

class LogradouroList(generics.ListCreateAPIView):
    queryset = Logradouro.objects.all()
    serializer_class = LogradouroSerializer

class LogradouroCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logradouro.objects.all()
    serializer_class = LogradouroSerializer

class PessoaFisicaList(generics.ListCreateAPIView):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializerCompleto

class PessoasCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer

class EnderecoPessoaFisicaList(generics.ListCreateAPIView):
    queryset = EnderecoPessoaFisica.objects.all()
    serializer_class = EnderecoPessoaFisicaSerializer




#######################################################
########### VIEWS DE ENDEREÇAMENTO ####################
#######################################################

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class CidadesListView(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        cidades = Cidade.objects.all().order_by('id').values()
        context = {
            'cidades' : cidades,
            'page_title' : 'Cadastro de Cidades'
        }
        return render(request,"cadastros/cidades/list_cidades.html", context=context)


class PessoasListView(View, LoginRequiredMixin):
    login_url = '/users/login/'
    def get(self,request):
        pessoas = PessoaFisica.objects.all().order_by('id').values()
        context = {
            'pessoas' : pessoas,
            'page_title' : 'Cadastro de Pessoas'
        }
        return render(request,"cadastros/pessoas/list_pessoas.html", context=context)


from django.urls import reverse_lazy
from .forms import PessoaFisicaModalForm
from .models import PessoaFisica
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView, BSModalUpdateView, BSModalDeleteView
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView

class PessoaFisicaInLine():
    form_class = PessoaFisicaModalForm
    model = PessoaFisica
    template_name = "cadastros/pessoa/create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('cadastros:list_pessoas')

    def formset_endereco_valid(self, formset):

        enderecos = formset.save(commit=False)  
        # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for endereco in enderecos:
            endereco.pessoa = self.object
            endereco.save()

    def formset_contato_valid(self, formset):
        
        contatos = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for contato in contatos:
            contato.pessoa = self.object
            contato.save()

class PessoaFisicaCreateView(PessoaFisicaInLine, BSModalCreateView,LoginRequiredMixin):
    login_url = '/user/login/'
    template_name = 'cadastros/pessoas/create.html'
    form_class = PessoaFisicaModalForm
    success_message = 'Pessoa cadastrada com sucesso.'
    success_url = reverse_lazy('cadastros:list_pessoas')
    
    def get_context_data(self, **kwargs):
        ctx = super(PessoaFisicaCreateView, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'enderecos': EnderecoFormSet(prefix='enderecos'),
                'contatos': ContatoFormSet(prefix='contatos'),
            }
        else:
            return {
                'enderecos': EnderecoFormSet(self.request.POST or None, self.request.FILES or None, prefix='enderecos'),
                'contatos': ContatoFormSet(self.request.POST or None, self.request.FILES or None, prefix='contatos'),
            }
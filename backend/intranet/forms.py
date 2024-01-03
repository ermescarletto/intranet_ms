from .models import PerfilColaborador
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

class PerfilUserForm(BSModalModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : 'text',
                'readonly' : True,
                
            }
        ),
        label='Nome'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : 'text',
                     'readonly' : True,
            }
        ),
        label='Sobrenome'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'type' : 'email',
                     'readonly' : True,
            }
        ),
        label='E-mail'
    )
    
    

    

    class Meta:
        model = PerfilColaborador
        fields = [
                  'first_name',
                  'last_name',
                  'email',
                  'unidade',
                  'departamento',
                  'cargo',
                  'imagem'
                  ]



class PerfilColaboradorForm(BSModalModelForm):
    class Meta:
        model = PerfilColaborador
        fields = [
                  'unidade',
                  'departamento',
                  'cargo',
                  'imagem'
                  ]

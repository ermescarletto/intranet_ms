from .models import User
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

class UserForm(BSModalModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : 'text'
            }
        ),
        label='Nome'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : 'text'
            }
        ),
        label='Sobrenome'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'type' : 'email',
                
            }
        ),
        label='E-mail'
    )
    cpf = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'type' : 'text',
                'data-mask':"000.000.000-00"
            }
        ),
        label='CPF'
    )
    telefone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'type' : 'text',
                'data-mask':"##-#########"
            }
        ),
        label='Telefone'
    )
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class' : 'form-control',
                'type' : 'date',
                
            }
        ),
        label='Data de Nascimento'
    )
    

    

    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'email',
                  'cpf',
                  'telefone',
                  'data_nascimento',
                  ]
        
        

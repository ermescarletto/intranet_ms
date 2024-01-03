from .models import PessoaFisica, EnderecoPessoaFisica, ContatoPessoaFisica
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from django.forms import inlineformset_factory


class EnderecoPessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = EnderecoPessoaFisica
        fields = [
            'tipo_endereco',
            'logradouro',
            'bairro',
            'cidade',
            'numero',
            'cep',
        ]
class ContatoPessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = ContatoPessoaFisica
        exclude = ('pessoa',)  # Exclude the pessoa field



class PessoaFisicaModalForm(BSModalModelForm):
    
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-outlined'}
        ),
        label='Nome'
    )
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
                  attrs={'class' : 'form-control',
                         'type' : 'date'}
        )
        ,label='Data Nascimento'
    )
    cpf = forms.CharField(
         widget=forms.TextInput(
              attrs={
                   'class' : 'form-control form-outlined',
              }
         )
    )
    sexo = forms.CharField(
         widget=forms.Select(
              
              choices= 
        (
		('M','MASCULINO'),('F','FEMININO')
		)              ,
              attrs={
                   'class' : 'form-control form-outlined',
              }
         )
    )
    
    
    email = forms.EmailField(
         widget=forms.EmailInput(
              attrs={
                   'class' : 'form-control form-outlined'
              }
         )
    )

    telefone = forms.CharField(
         widget=forms.TextInput(
              attrs={
                   'class' : 'form-control form-outlined',
                   'data-mask':"00-00000-0000"
              }
         )
    )
    class Meta:
        model = PessoaFisica
        fields = [
             'nome',
             'data_nascimento',
             'cpf',
             'sexo',
             'email',
             'telefone'
            ]
        

EnderecoFormSet = inlineformset_factory(
    PessoaFisica, EnderecoPessoaFisica, form=EnderecoPessoaFisicaForm, extra=1
)

ContatoFormSet = inlineformset_factory(
    PessoaFisica, ContatoPessoaFisica, form=ContatoPessoaFisicaForm, extra=1
)

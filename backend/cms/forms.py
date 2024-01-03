from .models import BannerCampanha
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

class BannerCampanhaModelForm(BSModalModelForm):
    titulo_campanha = forms.CharField(
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-outlined'}
        ),
        label='Título'
    )
    slogan_campanha = forms.CharField(
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-outlined'}
        ),
        label='Texto'
    )

    data_inicial = forms.DateField(
        widget=forms.DateInput(
                  attrs={'class' : 'form-control',
                         'type' : 'date'}
        )
        ,label='Data Inicial'
    )
    data_final = forms.DateField(
        widget=forms.DateInput(
                  attrs={'class' : 'form-control',
                         'type' : 'date'}
        )
        ,label='Data Final'
    )


    ativo = forms.BooleanField(

        )
    exibir_texto = forms.BooleanField(
        required=False
        )
    imagem_campanha = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "form-control form-outlined"})
        )
    class Meta:
        model = BannerCampanha
        fields = [
            'titulo_campanha',
            'slogan_campanha',
            'data_inicial',
            'data_final',
            'ativo',
            'exibir_texto',
            'imagem_campanha',
            ]
        
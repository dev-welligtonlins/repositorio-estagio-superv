from django import forms
from django.forms import ModelForm
from .models import RelatoriosMon, RelatoriosTut

class RelatoriosMonForm(ModelForm):

    class Meta:
        model = RelatoriosMon
        fields = ('relM_titulo', 'relM_data', 'relM_arquivo', 'relM_monitoria')
        labels = {
            'relM_titulo': 'Digite o nome do aviso',
            'relM_data': 'Defina a Data do aviso',
            'relM_arquivo': 'Anexe um arquivo abaixo',
            'relM_monitoria': 'Defina a monitoria relacionada',
        }
        widgets = {
            'relM_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'relM_data': forms.DateInput(attrs={'class':'form-control'}),
            'relM_arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }

class RelatoriosTutForm(ModelForm):

    class Meta:
        model = RelatoriosTut
        fields = ('relT_titulo', 'relT_data', 'relT_arquivo', 'relT_tutoria')
        labels = {
            'relT_titulo': 'Digite o nome do aviso',
            'relT_data': 'Defina a Data do aviso',
            'relT_arquivo': 'Anexe um arquivo abaixo',
            'relT_tutoria': 'Defina a tutoria relacionada',
        }
        widgets = {
            'relT_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'relT_data': forms.DateInput(attrs={'class':'form-control'}),
            'relT_arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }
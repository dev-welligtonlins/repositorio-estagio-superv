from django import forms
from django.forms import ModelForm
from .models import Avisos

class AvisosForm(ModelForm):

    class Meta:
        model = Avisos
        fields = ('avi_titulo', 'avi_descricao', 'avi_data', 'avi_arquivos', 'avi_administrador', 'avi_mostrar')
        labels = {
            'avi_titulo': 'Digite o nome do aviso',
            'avi_descricao': 'Digite a descricao do aviso',
            'avi_data': 'Defina a Data do aviso',
            'avi_arquivos': 'Anexe um arquivo abaixo',
            'avi_administrador': 'Defina o administrador',
            'avi_mostrar': 'Defina o estado de visualizacao',
        }
        widgets = {
            'avi_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'avi_descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descricao'}),
            'avi_data': forms.DateInput(attrs={'class':'form-control'}),
            'avi_arquivos': forms.FileInput(attrs={'class':'form-control'}),
            'avi_mostrar': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

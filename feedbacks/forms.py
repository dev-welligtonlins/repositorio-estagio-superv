from django import forms
from django.forms import ModelForm
from .models import Feedbacks

class FeedbacksForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_data', 'fee_arquivo', 'fee_acompanhamento')
        labels = {
            'fee_titulo': 'Digite o nome do aviso',
            'fee_descricao': 'Digite a descricao do aviso',
            'fee_data': 'Defina a Data do aviso',
            'fee_arquivo': 'Anexe um arquivo abaixo',
            'fee_acompanhamento': 'Defina o administrador',
        }
        widgets = {
            'fee_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descricao'}),
            'fee_data': forms.DateInput(attrs={'class':'form-control'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }

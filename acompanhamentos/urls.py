from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.acoIndex, name='acoIndex'),
    path('disciplinas', views.acoDisIndex, name='acoDisIndex'),
    path('monitorias', views.acoMonIndex, name='acoMonIndex'),
    path('tutorias', views.acoTutIndex, name='acoTutIndex'),
    path('interpretacoes', views.acoIntIndex, name='acoIntIndex'),
    path('adicionarAcompanhamento', views.adicionarAcompanhamento, name='adicionarAcompanhamento'),
    path('adicionarDisciplina', views.adicionarDisciplina, name='adicionarDisciplina'),
    path('adicionarMonitoria', views.adicionarMonitoria, name='adicionarMonitoria'),
    path('adicionarTutoria', views.adicionarTutoria, name='adicionarTutoria'),
    path('adicionarInterpretacao', views.adicionarInterpretacao, name='adicionarInterpretacao'),
    path('buscarAcompanhamento', views.buscarAcompanhamento, name='buscarAcompanhamento'),
    path('buscarDisciplina', views.buscarDisciplina, name='buscarDisciplina'),
    path('buscarMonitoria', views.buscarMonitoria, name='buscarMonitoria'),
    path('buscarTutoria', views.buscarTutoria, name='buscarTutoria'),
    path('buscarInterpretacao', views.buscarInterpretacao, name='buscarInterpretacao'),
    path('acompanhamento/<int:acompanhamento_id>', views.acompanhamento, name='acompanhamento'),
    path('atualizarAcompanhamento/<int:acompanhamento_id>', views.atualizarAcompanhamento, name='atualizarAcompanhamento'),
    path('atualizarDisciplina/<int:disciplina_id>', views.atualizarDisciplina, name='atualizarDisciplina'),
    path('atualizarMonitoria/<int:monitoria_id>', views.atualizarMonitoria, name='atualizarMonitoria'),
    path('atualizarTutoria/<int:tutoria_id>', views.atualizarTutoria, name='atualizarTutoria'),
    path('atualizarInterpretacao/<int:interpretacao_id>', views.atualizarInterpretacao, name='atualizarInterpretacao'),
    path('deletarAcompanhamento/<int:acompanhamento_id>', views.deletarAcompanhamento, name='deletarAcompanhamento'),
    path('deletarDisciplina/<int:disciplina_id>', views.deletarDisciplina, name='deletarDisciplina'),
    path('deletarMonitoria/<int:monitoria_id>', views.deletarMonitoria, name='deletarMonitoria'),
    path('deletarTutoria/<int:tutoria_id>', views.deletarTutoria, name='deletarTutoria'),
    path('deletarInterpretacao/<int:interpretacao_id>', views.deletarInterpretacao, name='deletarInterpretacao'),

]
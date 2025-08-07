from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('M', views.relMIndex, name='relMIndex'),
    path('T', views.relTIndex, name='relTIndex'),
    path('adicionarRelatorioM', views.adicionarRelatorioM, name='adicionarRelatorioM'),
    path('adicionarRelatorioT', views.adicionarRelatorioT, name='adicionarRelatorioT'),
    path('buscarRelatorioM', views.buscarRelatorioM, name='buscarRelatorioM'),
    path('buscarRelatorioT', views.buscarRelatorioT, name='buscarRelatorioT'),
    path('relatorioM/<int:relatorioM_id>', views.relatorioM, name='relatorioM'),
    path('relatorioT/<int:relatorioT_id>', views.relatorioT, name='relatorioT'),
    path('atualizarRelatorioM/<int:relatorioM_id>', views.atualizarRelatorioM, name='atualizarRelatorioM'),
    path('atualizarRelatorioT/<int:relatorioT_id>', views.atualizarRelatorioT, name='atualizarRelatorioT'),
]
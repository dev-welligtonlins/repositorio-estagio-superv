from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.aviIndex, name='aviIndex'),
    path('adicionarAviso', views.adicionarAviso, name='adicionarAviso'),
    path('buscarAviso', views.buscarAviso, name='buscarAviso'),
    path('aviso/<int:aviso_id>', views.aviso, name='aviso'),
    path('atualizarAviso/<int:aviso_id>', views.atualizarAviso, name='atualizarAviso'),
    path('deletarAviso/<int:aviso_id>', views.deletarAviso, name='deletarAviso'),

#ALUNO
    path('aviIndexAluno', views.aviIndexAluno, name='aviIndexAluno'),
    path('aviso/avisoAluno', views.aviso, name='avisoAluno'),
    path('buscarAvisoAluno', views.buscarAvisoAluno, name='buscarAvisoAluno'),
    path('avisoAluno/<int:aviso_id>', views.avisoAluno, name='avisoAluno'),
]
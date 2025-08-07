from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.feeIndex, name='feeIndex'),
    path('adicionarFeedback', views.adicionarFeedback, name='adicionarFeedback'),
    path('buscarFeedback', views.buscarFeedback, name='buscarFeedback'),
    path('feedback/<int:feedback_id>', views.feedback, name='feedback'),
    path('atualizarFeedback/<int:feedback_id>', views.atualizarFeedback, name='atualizarFeedback'),

]
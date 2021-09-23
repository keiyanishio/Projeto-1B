from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deletar/<int:ide>', views.deletar, name='deletar'),
    path('editar/<int:ide>', views.editar, name='editar'),
]
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name = "Inicio"),
    path('libros/', views.libros, name = "Libros"),
    path('autores/', views.autores, name = "Autores"),
    path('librosFormulario/', views.libros_formulario, name = "Libros formulario"),
    path('autoresFormulario/', views.autores_formulario, name = "Autores formulario"),
    path('generoFormulario/', views.genero_formulario, name = "Genero formulario"),
]
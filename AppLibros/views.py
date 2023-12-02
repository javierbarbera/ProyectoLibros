from django.shortcuts import render
from django.http import HttpResponse
from AppLibros.models import Libro, Autor, Genero

# Create your views here.

def inicio(request):
    return render(request, "AppLibros/inicio.html")

def libros(request):
    return render(request, "AppLibros/libros.html")

def autores(request):
    return render(request, "AppLibros/autores.html")

def libros_formulario(request):
    if request.method == "POST":
        libro = Libro(request.POST["titulo"], request.POST["autor"], request.POST["genero"], request.POST["sinopsis"])
        libro.save()
        return render(request, "AppLibros/inicio.html" )
    
    return render(request, "AppLibros/libros_formulario.html")

def autores_formulario(request):
    if request.method == "POST":
        autor = Autor(request.POST["nombre"], request.POST["apellido"])
        autor.save()
        return render(request, "AppLibros/inicio.html" )
    
    return render(request, "AppLibros/autores_formulario.html")

def genero_formulario(request):
    return render(request, "AppLibros/genero_formulario.html")
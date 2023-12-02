from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Genero(models.Model):
    CIENCIA_FICCION_FANTASIA = 'Ciencia Ficción y Fantasía'
    CLASICOS = "Clásicos"
    NOVELA = "Novela"
    POESIA = "Poesía"
    CUENTOS = "Cuentos"

    def __str__(self):
        return self.nombre
    
    OPCIONES_GENERO = [
        (CIENCIA_FICCION_FANTASIA, 'Ciencia Ficción y Fantasía'),
        (CLASICOS, 'Clásicos'),
        (NOVELA, 'Novela'),
        (POESIA, 'Poesía'),
        (CUENTOS, "Cuentos")
    ]

    nombre = models.CharField(max_length=100, choices=OPCIONES_GENERO, default=NOVELA)

    
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopsis = models.TextField()
   
    def __str__(self):
        return self.titulo
  
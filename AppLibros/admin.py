from django.contrib import admin


from AppLibros import models

admin.site.register(models.Autor)
admin.site.register(models.Libro)
admin.site.register(models.Genero)


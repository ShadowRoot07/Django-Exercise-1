from django.contrib import admin
from .models import Tarea, Categoria

admin.site.register(Categoria)
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'completada', 'fecha_creacion')
    list_filter = ('completada', 'categoria') # Añade filtros laterales
    search_fields = ('titulo',) # Añade una barra de búsqueda


from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )

    PRIORIDAD_CHOICES = [
        ('B', 'Baja'),
        ('M', 'Media'),
        ('A', 'Alta'),
    ]
    prioridad = models.CharField(
        max_length=1,
        choices=PRIORIDAD_CHOICES,
        default='M',
    )

    class Meta:
        ordering = ['-fecha_creacion'] # El '-' significa descendente (la más nueva primero)
        verbose_name_plural = "Mis Tareas" # Para que el Admin no diga "Tareas" sino algo personalizado

    def __str__(self):
        return self.titulo


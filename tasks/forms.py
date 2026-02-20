from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada', 'categoria', 'prioridad']
        # Esto le da "estilo" o comportamiento a los campos
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe aquí...'}),
            'titulo': forms.TextInput(attrs={'class': 'mi-clase-css'}),
        }


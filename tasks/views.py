from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Tarea
from .forms import TareaForm

# Añadimos 'nombre' como parámetro
def hola_mundo(request, nombre):
    # Usamos una f-string para insertar el nombre en el HTML
    return HttpResponse(f"<h1>¡Hola {nombre}!</h1><p>Bienvenido al calabozo de Django.</p>")


def lista_tareas(request):
    tareas = Tarea.objects.all()
    
    # Convertimos el QuerySet a una lista de diccionarios
    data = []
    for t in tareas:
        data.append({
            'id': t.id,
            'titulo': t.titulo,
            'completada': t.completada,
            'categoria': t.categoria.nombre if t.categoria else None
        })

    return render(request, 'tasks/lista.html', {'mis_tareas': tareas})
        


def detalle_tarea(request, id):
    print(f"DEBUG: Buscando ID {id} en la base de datos...")
    # Intentamos obtener la tarea. Si falla, Django lanza Http404 automáticamente.
    tarea = get_object_or_404(Tarea, id=id)
    
    data = {
        'id': tarea.id,
        'titulo': tarea.titulo,
        'descripcion': tarea.descripcion,
        'completada': tarea.completada,
        'categoria': tarea.categoria.nombre if tarea.categoria else "Sin categoría"
    }
    return render(request, 'tasks/detalle.html', {
        'tarea': tarea
    })


def crear_tarea(request):
    # Eliminamos el get_object_or_404 porque estamos CREANDO, no editando.
    
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:lista_tareas') 
    else:
        form = TareaForm()

    return render(request, 'tasks/crear.html', {'mi_formulario': form})


def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        # 'instance=tarea' es el secreto: le dice a Django que no cree una nueva, 
        # sino que actualice la que ya encontramos.
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tasks:lista_tareas')
    else:
        # Aquí cargamos el formulario con los datos actuales de la tarea
        form = TareaForm(instance=tarea)
        
    return render(request, 'tasks/crear.html', {'mi_formulario': form, 'editando': True})


def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tasks:lista_tareas')
    return render(request, 'tasks/confirmar_eliminacion.html', {'tarea': tarea})


def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        # Al pasarle la instancia, Django sabe que debe SOBREESCRIBIR ese registro
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tasks:lista_tareas')
    else:
        # Cargamos el form con los datos de la tarea encontrada
        form = TareaForm(instance=tarea)
    
    # Reutilizamos crear.html, pero pasamos una variable 'editando'
    return render(request, 'tasks/crear.html', {'mi_formulario': form, 'editando': True})


def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tasks:lista_tareas')
    
    return render(request, 'tasks/confirmar_eliminacion.html', {'tarea': tarea})


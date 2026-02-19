from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages

from .models import Tarea
from .forms import TareaForm


# Añadimos 'nombre' como parámetro
def hola_mundo(request, nombre):
    # Usamos una f-string para insertar el nombre en el HTML
    return HttpResponse(f"<h1>¡Hola {nombre}!</h1><p>Bienvenido al calabozo de Django.</p>")


@user_passes_test(lambda u: u.is_staff)
def vista_secreta_admin(request):
    return HttpResponse("Bienvenido al panel de control, ShadowRoot07")


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


@login_required
def crear_tarea(request):
    # Eliminamos el get_object_or_404 porque estamos CREANDO, no editando.
    
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, '¡Felicidades ShadowRoot07! La tarea fue creada con éxito.')

            return redirect('tasks:lista_tareas') 
    else:
        form = TareaForm()

    return render(request, 'tasks/crear.html', {'mi_formulario': form})


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

@require_POST
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('tasks:lista_tareas')
    
    return render(request, 'tasks/confirmar_eliminacion.html', {'tarea': tarea})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return redirect('tasks:lista_tareas')
    else:
        form = AuthenticationForm()
    
    return render(request, 'tasks/login.html', {'mi_formulario': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('tasks:lista_tareas')

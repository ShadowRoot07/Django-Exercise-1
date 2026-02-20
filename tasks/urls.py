# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TareaListView.as_view(), name='lista_tareas'),
    path('api/tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('api/tareas/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('api/tareas/editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('api/tareas/eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('login/', views.iniciar_sesion, name='login'),
path('logout/', views.cerrar_sesion, name='logout'),
]


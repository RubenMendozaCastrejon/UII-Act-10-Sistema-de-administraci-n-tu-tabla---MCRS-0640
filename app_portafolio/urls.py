from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'), # Lista todos los portafolios
  path('portafolio/<int:id_portafolio>/', views.view_portafolio, name='view_portafolio'), # Ver detalles de un portafolio específico
  path('portafolio/add/', views.add_portafolio, name='add_portafolio'), # Añadir un nuevo portafolio
  path('portafolio/edit/<int:id_portafolio>/', views.edit_portafolio, name='edit_portafolio'), # Editar un portafolio existente
  path('portafolio/delete/<int:id_portafolio>/', views.delete_portafolio, name='delete_portafolio'), # Eliminar un portafolio
]
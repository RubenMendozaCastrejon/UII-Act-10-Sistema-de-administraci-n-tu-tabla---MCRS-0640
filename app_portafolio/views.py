from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from datetime import datetime # Necesario para manejar el campo 'fecha'

from .models import Portafolio
from .forms import PortafolioForm


# Vista para listar todos los portafolios
def index(request):
  return render(request, 'students/index.html', { # Cambiado a 'index.html' sin subcarpeta
    'portafolios': Portafolio.objects.all().order_by('-fecha') # Obtiene todos los portafolios, ordenados por fecha
  })


# Vista para ver los detalles de un portafolio específico (usado en el modal de index.html)
# Si tuvieras una página de detalles separada, aquí se renderizaría un template específico.
# Actualmente, el botón de "ver" en index.html solo abre un modal, no navega a esta vista.
# Sin embargo, la mantengo por si decides tener una página de detalles en el futuro.
def view_portafolio(request, id_portafolio):
  portafolio = get_object_or_404(Portafolio, pk=id_portafolio)
  # Si tuvieras un template 'view_portafolio.html' para mostrar detalles en una página separada:
  # return render(request, 'view_portafolio.html', {'portafolio': portafolio})
  # Por ahora, redirige al índice ya que los detalles se muestran en un modal
  return HttpResponseRedirect(reverse('index'))


# Vista para añadir un nuevo portafolio
def add_portafolio(request):
  if request.method == 'POST':
    form = PortafolioForm(request.POST)
    if form.is_valid():
      # No hay necesidad de extraer campo por campo si usas form.save()
      # Si id_portafolio es autogenerado por tu lógica de negocio antes de guardar,
      # lo manejarías aquí. Si el usuario lo introduce, el formulario ya lo maneja.
      # Para este ejemplo, form.save() funcionará.
      form.save() # Guarda el objeto Portafolio directamente desde el formulario
      return render(request, 'students/add_portafolio.html', {
        'form': PortafolioForm(), # Crea un nuevo formulario vacío para futuras adiciones
        'success': True
      })
  else:
    form = PortafolioForm() # Crea un formulario vacío para el método GET
  return render(request, 'students/add_portafolio.html', {
    'form': form # Pasa el formulario (vacío o con errores de validación)
  })


# Vista para editar un portafolio existente
def edit_portafolio(request, id_portafolio):
  portafolio = get_object_or_404(Portafolio, pk=id_portafolio) # Obtiene el portafolio por su PK
  if request.method == 'POST':
    form = PortafolioForm(request.POST, instance=portafolio) # Pasa la instancia para pre-llenar y actualizar
    if form.is_valid():
      form.save() # Guarda los cambios en el objeto Portafolio existente
      return render(request, 'students/edit_portafolio.html', {
        'form': form, # Muestra el formulario con los datos actualizados
        'success': True
      })
  else:
    form = PortafolioForm(instance=portafolio) # Pre-llena el formulario con los datos del portafolio
  return render(request, 'students/edit_portafolio.html', {
    'form': form
  })


# Vista para eliminar un portafolio
def delete_portafolio(request, id_portafolio):
  if request.method == 'POST':
    portafolio = get_object_or_404(Portafolio, pk=id_portafolio) # Obtiene el portafolio por su PK
    portafolio.delete() # Elimina el objeto
  return HttpResponseRedirect(reverse('index')) # Redirige al índice después de la eliminación
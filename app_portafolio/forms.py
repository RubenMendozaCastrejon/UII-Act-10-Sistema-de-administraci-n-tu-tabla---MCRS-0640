from django import forms
from .models import Portafolio

class PortafolioForm(forms.ModelForm):
  class Meta:
    model = Portafolio
    # Excluimos 'id_portafolio' ya que es la PK y generalmente no se edita directamente en un formulario de creación/edición,
    # aunque en tu caso es un IntegerField y no un AutoField, por lo que podrías incluirlo si necesitas que el usuario lo ingrese.
    # Si quieres que el usuario lo ingrese, inclúyelo en 'fields'.
    fields = ['id_usuario', 'nombre', 'fecha', 'descripcion', 'valor_total']
    labels = {
      'id_usuario': 'ID de Usuario',
      'nombre': 'Nombre del Portafolio',
      'fecha': 'Fecha',
      'descripcion': 'Descripción',
      'valor_total': 'Valor Total',
    }
    widgets = {
      'id_usuario': forms.NumberInput(attrs={'class': 'form-control'}),
      'nombre': forms.TextInput(attrs={'class': 'form-control'}),
      # Para 'fecha', un DateTimeInput es más apropiado.
      # Puedes usar un widget personalizado para un mejor control del formato o un DateInput si solo te interesa la fecha.
      'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
      'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
      'valor_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), # 'step' para decimales
    }
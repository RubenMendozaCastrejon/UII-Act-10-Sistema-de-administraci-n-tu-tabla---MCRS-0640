from django.db import models

class Portafolio(models.Model):
    id_portafolio = models.IntegerField(primary_key=True)
    id_usuario = models.IntegerField()
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Portafolio' # Asegúrate de que el nombre de la tabla en la base de datos coincida
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'

    def __str__(self):
        return self.nombre
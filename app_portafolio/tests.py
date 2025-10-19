import random
from decimal import Decimal
from django.test import TestCase
from .models import Portafolio
from datetime import datetime

class PortafolioModelUnitTestCase(TestCase):
    def setUp(self):
        # Genera un id_portafolio único y un id_usuario aleatorio
        self.portafolio = Portafolio.objects.create(
            id_portafolio=random.randint(1000, 9999), # Genera un ID de portafolio aleatorio para pruebas
            id_usuario=random.randint(1, 100),       # ID de usuario aleatorio
            nombre='Portafolio de Prueba',
            fecha=datetime.now(),                    # Fecha y hora actual
            descripcion='Descripción de un portafolio de prueba para el test unitario.',
            valor_total=Decimal('12345.67')          # Valor total en formato Decimal
        )

    def test_portafolio_model_instance(self):
        """
        Verifica que el objeto creado en setUp sea una instancia del modelo Portafolio.
        """
        data = self.portafolio
        self.assertIsInstance(data, Portafolio)

    def test_portafolio_str_representation(self):
        """
        Verifica que el método __str__ del modelo Portafolio funcione correctamente.
        """
        data = self.portafolio
        self.assertEqual(str(data), 'Portafolio de Prueba')

    def test_portafolio_fields_data(self):
        """
        Verifica que los datos almacenados en los campos del portafolio sean correctos.
        """
        data = self.portafolio
        self.assertEqual(data.nombre, 'Portafolio de Prueba')
        self.assertEqual(data.valor_total, Decimal('12345.67'))
        self.assertIsNotNone(data.id_portafolio)
        self.assertIsNotNone(data.id_usuario)
        self.assertIsInstance(data.fecha, datetime)
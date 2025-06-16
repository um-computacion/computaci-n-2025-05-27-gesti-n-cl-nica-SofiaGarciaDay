import unittest
from modelo.modelo_paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_valida(self):
        p = Paciente("Lucía Gómez", "99887766", "05/05/1995")
        self.assertEqual(p.obtener_dni(), "99887766")
        self.assertIn("Lucía Gómez", str(p))

    def test_dni_invalido(self):
        with self.assertRaises(ValueError):
            Paciente("Tomás", "DNI-999", "15/08/1988")

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            Paciente("Tomás", "11223344", "1988-08-15")

    def test_fecha_futura(self):
        with self.assertRaises(ValueError):
            Paciente("Tomás", "11223344", "10/10/2999")
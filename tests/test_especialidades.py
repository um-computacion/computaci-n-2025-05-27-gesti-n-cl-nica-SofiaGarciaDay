import unittest
from modelo.modelo_especialidades import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_creacion_valida(self):
        e = Especialidad("Dermatología", ["martes", "viernes"])
        self.assertTrue(e.verificar_dia("martes"))
        self.assertFalse(e.verificar_dia("jueves"))
        salida = str(e)
        self.assertIn("Dermatología", salida)
        self.assertIn("martes", salida)

    def test_lista_dias_vacia(self):
        with self.assertRaises(ValueError):
            Especialidad("Neurología", [])

    def test_dia_invalido(self):
        with self.assertRaises(ValueError):
            Especialidad("Traumatología", ["caturday"])
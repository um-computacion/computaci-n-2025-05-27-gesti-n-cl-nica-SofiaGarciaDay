import unittest
from modelo.modelo_medico import Medico
from modelo.modelo_especialidades import Especialidad

class TestMedico(unittest.TestCase):
    def test_creacion_valida_sin_especialidades(self):
        m = Medico("Dra. Martínez", "M123")
        self.assertEqual(m.obtener_matricula(), "M123")

    def test_agregar_especialidad(self):
        m = Medico("Dra. Martínez", "M123")
        e1 = Especialidad("Neurología", ["miércoles"])
        m.agregar_especialidad(e1)
        self.assertIn("Neurología", str(m))

    def test_especialidad_duplicada(self):
        m = Medico("Dra. Martínez", "M123")
        e1 = Especialidad("Neurología", ["miércoles"])
        e2 = Especialidad("Neurología", ["jueves"])
        m.agregar_especialidad(e1)
        with self.assertRaises(ValueError):
            m.agregar_especialidad(e2)

    def test_obtener_especialidad_para_dia(self):
        e1 = Especialidad("Neurología", ["miércoles"])
        e2 = Especialidad("Dermatología", ["viernes"])
        m = Medico("Dra. Martínez", "M123", [e1, e2])
        self.assertEqual(m.obtener_especialidad_para_dia("viernes"), "Dermatología")
        self.assertIsNone(m.obtener_especialidad_para_dia("lunes"))
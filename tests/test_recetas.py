import unittest
from modelo.modelo_recetas import Receta
from modelo.modelo_paciente import Paciente
from modelo.modelo_medico import Medico
from modelo.modelo_especialidades import Especialidad
from modelo.modelo_excepciones import RecetaInvalidaException

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.p = Paciente("Luis Ramírez", "99887766", "15/03/1985")
        e = Especialidad("Dermatología", ["miércoles"])
        self.m = Medico("Dra. Fernández", "M998", [e])

    def test_creacion_receta_valida(self):
        r = Receta(self.p, self.m, ["Amoxicilina", "Cetirizina"])
        self.assertIn("Amoxicilina", str(r))
        self.assertIn("Cetirizina", str(r))

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.p, self.m, [])

    def test_medicamento_vacio_en_lista(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.p, self.m, ["", "Clorfenamina"])
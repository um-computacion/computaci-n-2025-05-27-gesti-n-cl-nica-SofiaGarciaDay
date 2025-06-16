import unittest
from datetime import datetime, timedelta
from modelo.modelo_turnos import Turno
from modelo.modelo_paciente import Paciente
from modelo.modelo_medico import Medico
from modelo.modelo_especialidades import Especialidad

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.p = Paciente("Lucía Gómez", "98765432", "15/05/1985")
        e = Especialidad("Dermatología", ["miércoles", "jueves"])
        self.m = Medico("Dra. Martínez", "M789", [e])

    def test_creacion_turno_valido(self):
        fecha_futura = datetime.now() + timedelta(days=2)
        t = Turno(self.p, self.m, fecha_futura, "Dermatología")
        self.assertEqual(t.obtener_medico().obtener_matricula(), "M789")

    def test_turno_en_fecha_pasada(self):
        fecha_pasada = datetime.now() - timedelta(days=2)
        with self.assertRaises(ValueError):
            Turno(self.p, self.m, fecha_pasada, "Dermatología")

    def test_turno_especialidad_invalida(self):
        fecha_futura = datetime.now() + timedelta(days=2)
        with self.assertRaises(ValueError):
            Turno(self.p, self.m, fecha_futura, "")
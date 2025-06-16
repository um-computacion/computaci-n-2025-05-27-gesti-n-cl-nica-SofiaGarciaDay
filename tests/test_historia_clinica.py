import unittest
from datetime import datetime, timedelta
from modelo.modelo_historia_clinica import HistoriaClinica
from modelo.modelo_paciente import Paciente
from modelo.modelo_turnos import Turno
from modelo.modelo_recetas import Receta
from modelo.modelo_medico import Medico
from modelo.modelo_especialidades import Especialidad

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.p = Paciente("María", "456", "15/08/1975")
        self.hc = HistoriaClinica(self.p)
        e = Especialidad("Dermatología", ["miércoles"])
        self.m = Medico("Dra. López", "M456", [e])

    def test_agregar_y_obtener_turnos(self):
        fecha = datetime.now() + timedelta(days=3)
        t = Turno(self.p, self.m, fecha, "Dermatología")
        self.hc.agregar_turno(t)
        turnos = self.hc.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "M456")

    def test_agregar_y_obtener_recetas(self):
        r = Receta(self.p, self.m, ["Crema tópica"])
        self.hc.agregar_receta(r)
        recetas = self.hc.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIn("Crema tópica", str(recetas[0]))

    def test_historia_clinica_paciente_invalido(self):
        with self.assertRaises(ValueError):
            HistoriaClinica("TextoNoValido")
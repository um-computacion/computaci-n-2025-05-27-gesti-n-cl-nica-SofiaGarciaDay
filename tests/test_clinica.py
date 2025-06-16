import unittest
from datetime import datetime, timedelta
from modelo.modelo_clinica import Clinica
from modelo.modelo_paciente import Paciente
from modelo.modelo_medico import Medico
from modelo.modelo_especialidades import Especialidad
from modelo.modelo_excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.p = Paciente("Ana", "222", "15/05/1985")
        self.clinica.agregar_paciente(self.p)
        e = Especialidad("Dermatología", ["jueves", "viernes"])
        self.m = Medico("Dra. Paula", "M222", [e])
        self.clinica.agregar_medico(self.m)

    def test_agregar_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("Ana", "222", "15/05/1985"))

    def test_agregar_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("Dra. Paula", "M222"))

    def test_agendar_turno_exitoso(self):
        proximo_jueves = datetime.now() + timedelta(days=(3 - datetime.now().weekday()) % 7 or 7)
        self.clinica.agendar_turno("222", "M222", "Dermatología", proximo_jueves.replace(hour=9, minute=0, second=0, microsecond=0))
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_agendar_turno_paciente_no_existe(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("999", "M222", "Dermatología", fecha)

    def test_agendar_turno_medico_no_existe(self):
        fecha = datetime.now() + timedelta(days=1)
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("222", "MXYZ", "Dermatología", fecha)

    def test_agendar_turno_medico_no_disponible_dia(self):
        proximo_lunes = datetime.now() + timedelta(days=(0 - datetime.now().weekday()) % 7 or 7)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("222", "M222", "Dermatología", proximo_lunes)

    def test_agendar_turno_duplicado(self):
        proximo_viernes = datetime.now() + timedelta(days=(4 - datetime.now().weekday()) % 7 or 7)
        fecha = proximo_viernes.replace(hour=14, minute=0, second=0, microsecond=0)
        self.clinica.agendar_turno("222", "M222", "Dermatología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("222", "M222", "Dermatología", fecha)

    def test_emitir_receta_exitoso(self):
        self.clinica.emitir_receta("222", "M222", ["Crema A", "Loción B"])
        historia = self.clinica.obtener_historia_clinica_por_dni("222")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_paciente_no_existe(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("999", "M222", ["Crema X"])

    def test_emitir_receta_medico_no_existe(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("222", "MXYZ", ["Crema X"])

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("222", "M222", [])

    def test_obtener_historia_clinica_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica_por_dni("999")
        
    def test_obtener_pacientes_y_medicos(self):
        pacientes = self.clinica.obtener_pacientes()
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(len(medicos), 1)
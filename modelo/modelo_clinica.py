from datetime import datetime
from typing import List, Dict
from .modelo_paciente import Paciente
from .modelo_medico import Medico
from .modelo_turnos import Turno
from .modelo_recetas import Receta
from .modelo_historia_clinica import HistoriaClinica
from .modelo_excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
)
class Clinica:
    def __init__(self):
       
        self.__pacientes: Dict[str, Paciente] = {}
        self.__medicos: Dict[str, Medico] = {}
        self.__turnos: List[Turno] = []
        self.__historias_clinicas: Dict[str, HistoriaClinica] = {}

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"El paciente con DNI {dni} ya está registrado.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Ya hay un médico registrado con la matrícula {matricula}.")
        self.__medicos[matricula] = medico

    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No se encontró paciente con DNI {dni}.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No se encontró médico con matrícula {matricula}.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for t in self.__turnos:
            if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("Ese horario ya está reservado para el médico indicado.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        disponible = False
        for e in medico._Medico__especialidades:
            if e.obtener_especialidad().lower() == especialidad_solicitada.lower():
                if e.verificar_dia(dia_semana):
                    disponible = True
                break
        if not disponible:
            raise MedicoNoDisponibleException(
                f"El doctor no atiende la especialidad '{especialidad_solicitada}' el día {dia_semana}.")

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)

        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def obtener_turnos(self) -> list[Turno]:
        return list(self.__turnos)

    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]
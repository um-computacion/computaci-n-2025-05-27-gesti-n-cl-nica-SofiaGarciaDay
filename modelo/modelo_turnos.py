from datetime import datetime

class Turno:
   
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        if not hasattr(paciente, "obtener_dni"):
            raise ValueError("El objeto proporcionado como paciente no es válido.")
        if not hasattr(medico, "obtener_matricula"):
            raise ValueError("El objeto proporcionado como médico no es válido.")

        if not isinstance(fecha_hora, datetime):
            raise ValueError("El parámetro fecha_hora debe ser una instancia de datetime.")
        if fecha_hora < datetime.now():
            raise ValueError("No es posible asignar un turno en una fecha ya pasada.")
        self.__fecha_hora = fecha_hora

        if not especialidad or not especialidad.strip():
            raise ValueError("Debe especificarse una especialidad para el turno.")
        self.__especialidad = especialidad.strip()

        self.__paciente = paciente
        self.__medico = medico

    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (f"Turno(Paciente: {self.__paciente}, "
                f"Medico: {self.__medico}, "
                f"Especialidad: {self.__especialidad}, "
                f"FechaHora: {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')})")
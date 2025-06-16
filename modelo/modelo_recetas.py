from datetime import datetime
from .modelo_excepciones import RecetaInvalidaException

class Receta:
    
    def __init__(self, paciente, medico, medicamentos: list[str]):
        if not hasattr(paciente, "obtener_dni"):
            raise ValueError("El objeto paciente no es válido.")
        if not hasattr(medico, "obtener_matricula"):
            raise ValueError("El objeto médico no es válido.")
        if not medicamentos or not isinstance(medicamentos, list):
            raise RecetaInvalidaException("Debe proporcionar una lista de medicamentos no vacía.")
        for m in medicamentos:
            if not isinstance(m, str) or not m.strip():
                raise RecetaInvalidaException("Cada entrada en la lista de medicamentos debe ser una cadena con contenido.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = [m.strip() for m in medicamentos]
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        return (f"Receta emitida para: {self.__paciente}, "
                f"Profesional: {self.__medico}, "
                f"Prescripción: [{meds}], "
                f"Emitida el: {fecha_str}")
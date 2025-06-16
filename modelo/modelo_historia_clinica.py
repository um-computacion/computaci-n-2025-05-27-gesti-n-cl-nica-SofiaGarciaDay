from typing import List
from .modelo_paciente import Paciente

class HistoriaClinica:
    
    def __init__(self, paciente: Paciente):
        
        if not isinstance(paciente, Paciente):
            raise ValueError("El paciente debe ser una instancia válida de la clase Paciente")
        
        self.__paciente = paciente
        self.__turnos: List = []
        self.__recetas: List = []
    
    def agregar_turno(self, turno):
        from .modelo_turnos import Turno
        if not isinstance(turno, Turno):
            raise ValueError("Se debe proporcionar un objeto Turno válido.")
        self.__turnos.append(turno)
    
    def obtener_turnos(self) -> List:
        return list(self.__turnos)
    
    def agregar_receta(self, receta):
        from .modelo_recetas import Receta
        if not isinstance(receta, Receta):
            raise ValueError("Se debe proporcionar un objeto Receta válido.")
        self.__recetas.append(receta)
    
    def obtener_recetas(self) -> List:
        return list(self.__recetas)
    
    def __str__(self) -> str:
        turnos_str = "\n  ".join(str(t) for t in self.__turnos) or "No hay turnos registrados."
        recetas_str = "\n  ".join(str(r) for r in self.__recetas) or "No hay recetas registradas."
        return (f"Historia Clínica (Paciente: {self.__paciente})\n"
                f" Turnos:\n  {turnos_str}\n"
                f" Recetas:\n  {recetas_str}")
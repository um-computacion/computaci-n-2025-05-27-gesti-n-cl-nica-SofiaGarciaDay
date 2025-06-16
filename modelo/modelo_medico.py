from typing import List, Optional
from .modelo_especialidades import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: List[Especialidad] = None): 
       
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del médico no puede estar vacío.")
        self.__nombre = nombre.strip()
        
        if not matricula or not matricula.strip():
            raise ValueError("La matrícula del médico no puede estar vacía.")
        self.__matricula = matricula.strip()
        
        self.__especialidades = []
        if especialidades:
            for e in especialidades:
                if not isinstance(e, Especialidad):
                    raise ValueError("Cada especialidad debe ser una instancia de Especialidad.")
                
                if any(existing.obtener_especialidad().lower() == e.obtener_especialidad().lower() for existing in self.__especialidades):
                    raise ValueError(f"Especialidad duplicada: {e.obtener_especialidad()}.")
                self.__especialidades.append(e)
    
    def agregar_especialidad(self, especialidad: Especialidad):
        if not isinstance(especialidad, Especialidad):
            raise ValueError("Debe proporcionar un objeto Especialidad.")
       
        if any(existing.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower() for existing in self.__especialidades):
            raise ValueError(f"El médico ya tiene la especialidad {especialidad.obtener_especialidad()}.")
        self.__especialidades.append(especialidad)
    
    def obtener_matricula(self) -> str:
        return self.__matricula
    
    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
       
        for e in self.__especialidades:
            if e.verificar_dia(dia):
                return e.obtener_especialidad()
        return None
    
    def __str__(self) -> str:
        lista_str = [str(e) for e in self.__especialidades]
        return f"{self.__nombre}, {self.__matricula}, [{'; '.join(lista_str)}]"
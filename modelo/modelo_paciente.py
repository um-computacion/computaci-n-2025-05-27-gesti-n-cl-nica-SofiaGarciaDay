from datetime import datetime

class Paciente:
    
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
     
        if not nombre or not nombre.strip():
            raise ValueError("Debe ingresar un nombre válido para el paciente.")
        self.__nombre = nombre.strip()

        if not dni or not dni.isdigit():
            raise ValueError("El DNI debe contener únicamente números.")
        self.__dni = dni

        try:
            fecha_obj = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha de nacimiento debe estar en el formato dd/mm/aaaa.")
   
        if fecha_obj > datetime.now():
            raise ValueError("La fecha de nacimiento no puede ser posterior a la fecha actual.")
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"
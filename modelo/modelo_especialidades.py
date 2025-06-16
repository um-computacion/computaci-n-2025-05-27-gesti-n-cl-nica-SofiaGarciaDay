class Especialidad:
    DIAS_VALIDOS = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"}

    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not tipo.strip():
            raise ValueError("Debe proporcionarse un nombre válido para la especialidad.")
        self.__tipo = tipo.strip()

        if not dias or not isinstance(dias, list):
            raise ValueError("Se requiere una lista de días con al menos un elemento.")
        dias_normalizados = []
        for d in dias:
            if not isinstance(d, str):
                raise ValueError("Los días deben especificarse como cadenas de texto.")
            dia_lower = d.strip().lower()
            if dia_lower not in self.DIAS_VALIDOS:
                raise ValueError(f"'{d}' no es un día reconocido.")
            dias_normalizados.append(dia_lower)
        self.__dias = dias_normalizados

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        if not dia or not isinstance(dia, str):
            return False
        return dia.strip().lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Disponible los días: {dias_str})"
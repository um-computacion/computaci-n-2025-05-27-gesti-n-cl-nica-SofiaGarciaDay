class PacienteNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra un paciente con el DNI especificado."""
    pass

class MedicoNoEncontradoException(Exception):
    """Se lanza si no se puede ubicar un médico con la matrícula proporcionada."""
    pass

class MedicoNoDisponibleException(Exception):
    """Se utiliza cuando el médico no está disponible en la especialidad o día solicitado."""
    pass

class TurnoOcupadoException(Exception):
    """Se lanza si el horario del turno ya está ocupado por el mismo médico."""
    pass

class RecetaInvalidaException(Exception):
    """Indica que la receta proporcionada no cumple con los requisitos necesarios."""
    pass
from modelo.modelo_clinica import Clinica
from modelo.modelo_paciente import Paciente
from modelo.modelo_medico import Medico
from modelo.modelo_especialidades import Especialidad
from modelo.modelo_excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)
from datetime import datetime

class CLI:
    
    def __init__(self, clinica: Clinica):
        self.clinica = clinica

    def iniciar(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")
            
            try:
                opcion = input("Seleccione una opción: ").strip()
                
                if opcion == "1":
                    self._agregar_paciente()
                elif opcion == "2":
                    self._agregar_medico()
                elif opcion == "3":
                    self._agendar_turno()
                elif opcion == "4":
                    self._agregar_especialidad_medico()
                elif opcion == "5":
                    self._emitir_receta()
                elif opcion == "6":
                    self._ver_historia_clinica()
                elif opcion == "7":
                    self._ver_todos_turnos()
                elif opcion == "8":
                    self._ver_todos_pacientes()
                elif opcion == "9":
                    self._ver_todos_medicos()
                elif opcion == "0":
                    print("Saliendo…")
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
                    
            except KeyboardInterrupt:
                print("\n\nSaliendo…")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")

    def _agregar_paciente(self):
        try:
            nombre = input("Nombre completo: ").strip()
            dni = input("DNI: ").strip()
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            
            paciente = Paciente(nombre, dni, fecha_nac)
         
            self.clinica.agregar_paciente(paciente)
            print("Paciente agregado correctamente.")
            
        except (ValueError, PacienteNoEncontradoException) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def _agregar_medico(self):
        try:
            nombre = input("Nombre del médico: ").strip()
            matricula = input("Matrícula profesional: ").strip()
            
            lista_especialidades = []
            
            try:
                num_esp = int(input("¿Cuántas especialidades desea agregar? ").strip())
                if num_esp < 0:
                    raise ValueError("El número de especialidades debe ser positivo")
            except ValueError:
                raise ValueError("Debe ingresar un número válido de especialidades")
            
            for i in range(num_esp):
                print(f"\n--- Especialidad {i+1} ---")
                tipo = input("Tipo de especialidad: ").strip()
                dias_str = input("Días de atención (separados por comas): ").strip()
                
                dias = [d.strip().lower() for d in dias_str.split(",") if d.strip()]
                if not dias:
                    raise ValueError("Debe especificar al menos un día de atención")

                esp = Especialidad(tipo, dias)
                lista_especialidades.append(esp)
            
            medico = Medico(nombre, matricula, lista_especialidades)
            
            self.clinica.agregar_medico(medico)
            print("Médico agregado correctamente.")
            
        except (ValueError, MedicoNoDisponibleException) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def _agendar_turno(self):
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad: ").strip()
            fecha_hora_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ").strip()
            
            try:
                fecha_hora = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
            except ValueError:
                raise ValueError("Formato de fecha y hora inválido. Use dd/mm/aaaa HH:MM")
            
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado correctamente.")
            
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, 
                TurnoOcupadoException, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def _agregar_especialidad_medico(self):
        try:
            matricula = input("Matrícula del médico: ").strip()
            tipo = input("Tipo de especialidad: ").strip()
            dias_str = input("Días de atención (separados por comas): ").strip()
            
            dias = [d.strip().lower() for d in dias_str.split(",") if d.strip()]
            if not dias:
                raise ValueError("Debe especificar al menos un día de atención")
            
            esp = Especialidad(tipo, dias)
            
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            medico.agregar_especialidad(esp)
            print("Especialidad agregada correctamente.")
            
        except (MedicoNoDisponibleException, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def _emitir_receta(self):
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            meds_str = input("Medicamentos (separados por comas): ").strip()
            
            medicamentos = [m.strip() for m in meds_str.split(",") if m.strip()]
            if not medicamentos:
                raise RecetaInvalidaException("Debe especificar al menos un medicamento")
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida correctamente.")
            
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, 
                RecetaInvalidaException) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def _ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ").strip()
            
            historia = self.clinica.obtener_historia_clinica_por_dni(dni)
            print("\n" + "="*50)
            print(historia)
            print("="*50)
            
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def _ver_todos_turnos(self):
        try:
            turnos = self.clinica.obtener_turnos()
            
            if turnos:
                print("\n--- Todos los Turnos ---")
                print("-" * 80)
                for i, turno in enumerate(turnos, 1):
                    print(f"{i}. {turno}")
                print("-" * 80)
            else:
                print("No hay turnos registrados.")
                
        except Exception as e:
            print(f"Error: {e}")

    def _ver_todos_pacientes(self):
        try:
            pacientes = self.clinica.obtener_pacientes()
            
            if pacientes:
                print("\n--- Todos los Pacientes ---")
                print("-" * 50)
                for i, paciente in enumerate(pacientes, 1):
                    print(f"{i}. {paciente}")
                print("-" * 50)
            else:
                print("No hay pacientes registrados.")
                
        except Exception as e:
            print(f"Error: {e}")

    def _ver_todos_medicos(self):
        try:
            medicos = self.clinica.obtener_medicos()
            
            if medicos:
                print("\n--- Todos los Médicos ---")
                print("-" * 80)
                for i, medico in enumerate(medicos, 1):
                    print(f"{i}. {medico}")
                print("-" * 80)
            else:
                print("No hay médicos registrados.")
                
        except Exception as e:
            print(f"Error: {e}")
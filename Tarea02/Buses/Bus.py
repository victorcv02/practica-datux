class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []
        self.conductores_asignados = []

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            print(f"El bus {self.id_bus} ya tiene asignado ese horario.")

    def asignar_conductor(self, conductor, horario):
        # Validar que el conductor no tenga ese horario asignado ya
        if horario in conductor.horarios:
            print(f"El conductor {conductor.nombre} ya tiene un bus asignado en ese horario.")
        elif any(horario in c.horarios for c in self.conductores_asignados):
            print(f"Ya hay un conductor asignado para el horario {horario} en el bus {self.id_bus}.")
        else:
            self.conductores_asignados.append(conductor)
            conductor.agregar_horario(horario)
            print(f"Conductor {conductor.nombre} asignado al bus {self.id_bus} en el horario {horario}.")

    

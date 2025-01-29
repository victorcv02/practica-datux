class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios_bus = []  # AQUI GUARDAMOS LA LISTA DE LOS HORARIOS REGISTRADO PARA LOS BUSES
        self.conductores_asignados = []

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def agregar_horario(self, horario):
        if horario not in self.horarios_bus:
            self.horarios_bus.append(horario)
        else:
            print(f"El bus {self.id_bus} ya tiene asignado ese horario.")

    def asignar_conductor(self, conductor, horario_inicio, horario_fin):
        # Crear el rango de horarios
        horario = f"{horario_inicio} - {horario_fin}"
        
        # AQUI PODEMOS VALIDAR QUE UN CONDUCTOR NO TENGA EL MISMO HORARIO QUE OTRO
        if horario in conductor.horarios_conductor:
            print(f"El conductor {conductor.nombre} ya tiene un bus asignado en ese horario.")
        elif any(horario in c.horarios_conductor for c in self.conductores_asignados):
            print(f"Ya hay un conductor asignado para el horario {horario} en el bus {self.id_bus}.")
        else:
            self.conductores_asignados.append(conductor)
            conductor.agregar_horario(horario_inicio, horario_fin)
            print(f"Conductor {conductor.nombre} asignado al bus {self.id_bus} en el horario {horario}.")

class Conductor:
    def __init__(self, id_conductor, nombre):
        self.id_conductor = id_conductor  # Nuevo campo ID del conductor
        self.nombre = nombre
        self.horarios = []  # Horarios asignados al conductor (horas, no días ni fechas)

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            print(f"El conductor {self.nombre} ya tiene asignado ese horario.")
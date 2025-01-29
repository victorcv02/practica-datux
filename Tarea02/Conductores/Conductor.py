class Conductor:
    def __init__(self, id_conductor, nombre):
        self.id_conductor = id_conductor
        self.nombre = nombre
        self.horarios_conductor = []  # AQUI GUARDAMOS LA LISTA DE LOS HORARIOS REGISTRADO PARA LOS CONDUCTORES

    def agregar_horario(self, horario_inicio, horario_fin):
        # AQUI PODEMOS VALIDAR EL FORMATO EN HORAS
        if self.validar_horario(horario_inicio) and self.validar_horario(horario_fin):
            if not self.horario_superpuesto(horario_inicio, horario_fin):
                rango_horario = f"{horario_inicio} - {horario_fin}"
                self.horarios_conductor.append(rango_horario)
                print(f"Rango {rango_horario} asignado al conductor {self.nombre}.")
            else:
                print(f"Ya existe un conductor asignado en un horario superpuesto ({horario_inicio} - {horario_fin}).")
        else:
            print(f"Uno o ambos horarios no están en formato válido (HH:MM).")

    def validar_horario(self, horario):
        try:
            hora, minuto = map(int, horario.split(":"))
            return 0 <= hora < 24 and 0 <= minuto < 60
        except ValueError:
            return False

    def horario_superpuesto(self, nuevo_inicio, nuevo_fin):
        # CON ESTA PARTE SE CONVIERTE DE HORAS A MINUTO PARA PODER 
        # COMPARAR SI ES QUE HAY ALGUIEN DENTRO DE UN RANGO DE HORARIO
        nuevo_inicio_min = self.convertir_a_minutos(nuevo_inicio)
        nuevo_fin_min = self.convertir_a_minutos(nuevo_fin)

        for horario in self.horarios_conductor:
            horario_inicio, horario_fin = horario.split(" - ")
            horario_inicio_min = self.convertir_a_minutos(horario_inicio)
            horario_fin_min = self.convertir_a_minutos(horario_fin)

            if not (nuevo_fin_min <= horario_inicio_min or nuevo_inicio_min >= horario_fin_min):#CON ESTA PARTE PODEMOS VALIDAR PARA QUE NO SE SUPERPONGAN LOS HORARIOS
                return True
        return False

    def convertir_a_minutos(self, horario):
        hora, minuto = map(int, horario.split(":"))
        return hora * 60 + minuto

from Buses.Bus import *
from Conductores.Conductor import *

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self):
        print("----------------------------------------------")
        id_bus = input("Ingrese el ID del bus: ").upper() 
        bus = Bus(id_bus)
        self.buses.append(bus)
        print("----------------------------------------------")
        print(f"Bus {id_bus} agregado.")

    def agregar_ruta_a_bus(self):
        print("----------------------------------------------")
        id_bus = input("Ingrese el ID del bus: ").upper() 
        bus = self.encontrar_bus(id_bus)
        if bus:
            ruta = input("Ingrese la ruta del bus: ").upper() 
            bus.agregar_ruta(ruta)
            print("----------------------------------------------")
            print(f"Ruta {ruta} asignada al bus {id_bus}.")
        else:
            print("----------------------------------------------")
            print(f"Bus {id_bus} no encontrado.")

    def registrar_horario_bus(self):
        print("----------------------------------------------")
        id_bus = input("Ingrese el ID del bus: ").upper() 
        bus = self.encontrar_bus(id_bus)
        if bus:
            horario = input("Ingrese el horario (HH:MM): ")
            bus.agregar_horario(horario)
            print("----------------------------------------------")
            print(f"Horario {horario} asignado al bus {id_bus}.")
        else:
            print("----------------------------------------------")
            print(f"Bus {id_bus} no encontrado.")

    def agregar_conductor(self):
        print("----------------------------------------------")
        id_conductor = input("Ingrese el ID del conductor: ").upper() 
        nombre = input("Ingrese el nombre del conductor: ").upper() 
        conductor = Conductor(id_conductor, nombre)
        self.conductores.append(conductor)
        print("----------------------------------------------")
        print(f"Conductor {nombre} con ID {id_conductor} agregado.")

    def agregar_horario_conductor(self):
        print("----------------------------------------------")
        nombre = input("Ingrese el nombre del conductor: ").upper() 
        conductor = self.encontrar_conductor(nombre)
        if conductor:
            horario = input("Ingrese el horario (HH:MM): ")
            conductor.agregar_horario(horario)
            print("----------------------------------------------")
            print(f"Horario {horario} asignado al conductor {nombre}.")
        else:
            print("----------------------------------------------")
            print(f"Conductor {nombre} no encontrado.")

    def asignar_bus_a_conductor(self):
        print("----------------------------------------------")
        id_bus = input("Ingrese el ID del bus: ").upper() 
        bus = self.encontrar_bus(id_bus)
        if bus:
            id_conductor = input("Ingrese el ID del conductor: ")
            conductor = self.encontrar_conductor(id_conductor)
            if conductor:
                horario = input("Ingrese el horario (HH:MM): ")
                bus.asignar_conductor(conductor, horario)
            else:
                print("----------------------------------------------")
                print(f"Conductor {id_conductor} no encontrado.")
        else:
            print("----------------------------------------------")
            print(f"Bus {id_bus} no encontrado.")

    def encontrar_bus(self, id_bus):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                return bus
        return None

    def encontrar_conductor(self, id_conductor):
        for conductor in self.conductores:
            if conductor.id_conductor == id_conductor:
                return conductor
        return None
    
    def visualizar_conductores(self):
        if not self.conductores:
             print("----------------------------------------------")
             print("No hay conductores registrados.")
        else:
            for conductor in self.conductores:
                   print("----------------------------------------------")
                   print(f"\nConductor: {conductor.nombre} (ID: {conductor.id_conductor})")
            if conductor.horarios:
                for horario in conductor.horarios:
                    bus_asignado = None
                    # Buscando el bus asignado al conductor
                    for bus in self.buses:
                        if conductor in bus.conductores_asignados and horario in bus.horarios:
                            bus_asignado = bus
                            break
                    if bus_asignado:
                        print("----------------------------------------------")
                        print(f"  Bus asignado: {bus_asignado.id_bus}")
                        print(f"  Ruta del bus: {bus_asignado.ruta}")
                        print(f"  Horario: {horario}")
                    else:
                        print("----------------------------------------------")
                        print(f"  No hay bus asignado para el horario {horario}.")
            else:
                print("----------------------------------------------")
                print("  No tiene horarios asignados.")

    def menu(self):
        while True:
            print("\n--------------- MENU ITERATIVO ---------------")
            print("1. Agregar un bus")
            print("2. Agregar ruta a un bus")
            print("3. Registrar horario a un bus")
            print("4. Agregar un conductor")
            print("5. Agregar horario a un conductor")
            print("6. Asignar bus a un conductor")
            print("7. Visualizar conductores registrados")
            print("8. Salir")
            print("----------------------------------------------")
            opcion = input("Seleccione una opción: ")
            

            if opcion == '1':
                self.agregar_bus()
            elif opcion == '2':
                self.agregar_ruta_a_bus()
            elif opcion == '3':
                self.registrar_horario_bus()
            elif opcion == '4':
                self.agregar_conductor()
            elif opcion == '5':
                self.agregar_horario_conductor()
            elif opcion == '6':
                self.asignar_bus_a_conductor()
            elif opcion == '7':
                self.visualizar_conductores()
            elif opcion == '8':
                break
            else:
                print("Opción inválida. Intente nuevamente.")


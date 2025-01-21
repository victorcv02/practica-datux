# Escribir un programa que pida un numero entero y calcule la suma de 1 hasta el numero ingresado. 
# Usar la formula de suma de enteros

numero= int(input("Escribe algun numero entero: "))

sumadeenteros = (numero * (numero + 1)) // 2

print(f"La suma de los números de 1 hasta el {numero} es {sumadeenteros}.")

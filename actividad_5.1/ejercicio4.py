# Este programa determina si un número es divisible por 2 o por 5.

# Entrada
numero = int(input("Ingrese un número: "))

# Proceso y Salida
if numero % 2 == 0 or numero % 5 == 0:
    print("El número es divisible por 2 o por 5.")
else:
    print("El número no es divisible por 2 ni por 5.")

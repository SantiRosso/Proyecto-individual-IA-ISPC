# promedio_notas.py

def calcular_promedio(nota1, nota2, nota3, nota4, nota5):
    suma = nota1 + nota2 + nota3 + nota4 + nota5
    promedio = suma / 5
    return promedio

# Entradas
nota1 = float(input("Ingrese la nota de la materia 1: "))
nota2 = float(input("Ingrese la nota de la materia 2: "))
nota3 = float(input("Ingrese la nota de la materia 3: "))
nota4 = float(input("Ingrese la nota de la materia 4: "))
nota5 = float(input("Ingrese la nota de la materia 5: "))

# Cálculo del promedio
promedio = calcular_promedio(nota1, nota2, nota3, nota4, nota5)

# Salida
print(f"El promedio de las notas es: {promedio}")

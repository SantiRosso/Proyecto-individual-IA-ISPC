# Este programa pide al usuario que ingrese 10 nombres no repetidos, los guarda en una lista y los muestra.

nombres = []

while len(nombres) < 10:
    nombre = input("Ingrese un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("El nombre ya fue ingresado, por favor ingrese otro nombre.")

print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)

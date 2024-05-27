# Este programa elimina la tercera y la última persona de una lista de nombres, ordena la lista y la muestra.

nombres = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Elena', 'Felipe', 'Gabriela', 'Hugo', 'Ines', 'Jorge']

# Eliminar la tercera persona (índice 2) y la última persona (índice -1)
del nombres[2]
del nombres[-1]

# Ordenar la lista
nombres.sort()

# Mostrar la lista
print("Lista modificada y ordenada:")
for nombre in nombres:
    print(nombre)

"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
loteria =[]
#llenar la lista con los numeros de la loteria
for i in range(6):
    numero = int(input(f"ingrese el numero {i+1}: "))
    loteria.append(numero)

#ordenar la lista
loteria.sort()

#imprimir la lista
print(f"los numeros elegidos son: {loteria}")
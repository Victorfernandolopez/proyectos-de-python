"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
#creacion de la lista
lista_numeros = []

#almacenar los numeros del 1 al 10
for i in range(1,11):
    lista_numeros.append(i)

#invertir la lista
lista_numeros.reverse()

#imprimir la lista inversa
print(f"lista invertida: {lista_numeros}")
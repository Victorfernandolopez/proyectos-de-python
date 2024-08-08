"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
def media(lista):
    suma = 0
    for i in lista:
        suma+=i
    return suma/len(lista)

lista = [2,3,3,5,7,10]
print(media(lista))
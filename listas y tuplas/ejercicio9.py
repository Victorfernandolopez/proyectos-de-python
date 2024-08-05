"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
palabra = input("ingrese una palabra")
vocales = ["a","e","i","o","u"]

#recorrer la lista de vocales
for vocal in vocales:
    cont = 0
    #recorrer la palabra y comparar con la vocal
    for letra in palabra:
        if letra == vocal:
            cont+=1
    print(f"la vocal {vocal} aparece {cont} cantidad de veces")

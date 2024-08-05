"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
palabra = list(input("ingresa la palabra para analizar: "))
palabra_alrevez = palabra[::-1]
for i in range(len(palabra)):
    if palabra[i] != palabra_alrevez[i]:
        print(f"{palabra} no es un polindromo")
else:
    print(f"{palabra}es un polindromo")
"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

nuemro1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese el divisor: "))
cociente = nuemro1//numero2
resto = nuemro1%numero2
print(f"el cociente es: {cociente}")
print(f"el resto es: {resto}")

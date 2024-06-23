"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
"""

for i in range(1, 10, 2):  # i toma valores 1, 3, 5, 7, 9
    for j in range(i, 0, -2):  # j toma valores desde i hasta 1, decrementando de 2 en 2
        print(j, end=" ")
    print()  # Para nueva línea después de imprimir cada fila
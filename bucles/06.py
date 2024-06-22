"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
numero = int(input("ingrese una numero entero: "))
for i in range(5):
    print(str(numero)*(i+1))
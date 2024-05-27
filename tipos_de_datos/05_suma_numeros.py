"""
Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
"""
numero = int(input("ingrese un numero entero: "))
suma = 0
for i in range(1,numero+1):
    suma += i
print(suma)
"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""
def factorial(numero):
    factorial = numero
    for i in range(numero-1,1,-1):
        factorial *= i
    return factorial

print(factorial(5))
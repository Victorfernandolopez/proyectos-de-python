"""
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
def cuadrados(lista):
    cuadrados = []
    for i in lista:
        cuadrado= i*i
        cuadrados.append(cuadrado)
    return cuadrados

lista = [1,2,3,4,5,6,7,8,9]
lista_cuadrada = cuadrados(lista)

print(f"lista original: {lista}")
print(f"lista cuadrada: {lista_cuadrada}")
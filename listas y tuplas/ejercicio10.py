"""
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""
lista_precios = [50,75,46,22,80,65,8]

#ordenamos la lista de menor a mayor
lista_precios.sort()

print(f"el menor de los valores es {lista_precios[0]}")
print(f"el mayor de los valores es {lista_precios[len(lista_precios)-1]}")
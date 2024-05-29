"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
nombre_usuario = input("Ingrese su nombre: ")
numero = int(input("Ingrese un número: "))

for i in range(numero):
    print(nombre_usuario)

print("solucion 2")
print((nombre_usuario + "\n") * numero)
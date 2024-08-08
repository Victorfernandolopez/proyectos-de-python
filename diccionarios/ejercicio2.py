"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
datos = {}
datos['nombre']=input("ingrese su nombre: ")
datos['edad']=input("ingrese su edad: ")
datos['direccion'] = input("ingrese su direccion: ")
datos['telefono'] = input("ingrese su numero de telefono: ")

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}")

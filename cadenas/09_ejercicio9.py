"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
"""
fecha = input("ingrese su fecha de nacimiento con el formato (dd/mm/aaaa): ")
fecha_separada = fecha.split("/")
print(f"dia: {fecha_separada[0]}")
print(f"mes: {fecha_separada[1]}")
print(f"año: {fecha_separada[2]}")

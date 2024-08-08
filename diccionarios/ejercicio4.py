"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
#creacion de los meses del año
meses = {'enero' : '01', 'febrero': '02', 'marzo': '03', 'abril': '04','mayo': '05', 'junio': '06', 'julio': '07', 'agosto':  '08','septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'}

#solicitamos la fecha
fecha = input("ingrese una fecha en formato (dd/mm/aaaa): ")
#separar el string en una lista para poder utilizar el mes ingresado
fecha_separada = fecha.split('/')
#comparar el mes ingresado con el mes guardado en el diccionario y mostrar la fecha con su nombre
for clave,valor in meses.items():
    if valor == fecha_separada[1]:
        print(f"fecha: {fecha_separada[0]}/{clave}/{fecha_separada[2]}")


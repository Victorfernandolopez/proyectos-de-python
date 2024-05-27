"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
#definir el peso
peso_payasos = 112
peso_muniecas = 75

#solicitud al usuario
cant_payasos = int(input("ingrese la cantidad de payasos vendidos: "))
cant_muniecas = int(input("ingrese la cantidad de muñecas vendidas: "))

#calcular peso
peso_paquete = (cant_payasos*peso_payasos)+(cant_muniecas*peso_muniecas)

#mostrar peso
print(f"el peso total del paquete es: {peso_paquete} gramos")
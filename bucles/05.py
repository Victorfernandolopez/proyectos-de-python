"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
cant_invretir = float(input("ingrese la cantidad a invertir: "))
interes_anual = int(input("ingrese el interes anual: "))
years = int(input("ingrese la cantidad de años: "))
monto_final = 0
#convertir los intereces a decimal
interes_anual /= 100

#calcular intereses, sumarlos al total y mostrar el total por pantalla
for i in range(years):
    monto_final = cant_invretir*(1+interes_anual)**(i+1)
    print(f"total {i+1} año: {monto_final}")
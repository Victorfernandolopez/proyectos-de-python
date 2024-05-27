"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
inversion = float(input("ingrese la cantidad a invertir: "))
interes_anual = float(input("ingrese el interes anual: "))
cant_anos = int(input("ingrese la cantidad de años a invertir: "))
# Calcular el capital obtenido con interés compuesto
capital_final = inversion * (1 + interes_anual / 100) ** cant_anos
print(f"en {cant_anos} años su inversion mas el inters obtenido sera: {capital_final}")
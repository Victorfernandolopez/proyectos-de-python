"Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."

horas_trabajadas = int(input("cuantas horas trabaja: "))
valor_horas = float(input("cual es el valor hora: "))
print(f"total a pagar por horas trabajadas: {horas_trabajadas*valor_horas}")
"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
# Definir el interés anual
interes_anual = 0.04

# Solicitar al usuario la cantidad de dinero a depositar
deposito = float(input("Ingrese el monto a depositar en la cuenta: "))

# Inicializar el balance de la cuenta con el depósito inicial
cuenta = deposito

# Mostrar el balance inicial de la cuenta
print(f"Total de dinero en cuenta al inicio: {cuenta:.2f}")

# Calcular y mostrar el balance de la cuenta después de cada uno de los tres años
for i in range(1, 4):
    cuenta += cuenta * interes_anual
    print(f"Año {i}, dinero en cuenta: {cuenta:.2f}")
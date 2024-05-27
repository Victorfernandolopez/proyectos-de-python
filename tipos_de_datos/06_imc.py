"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
peso = float(input("ingrese su peso en kg: "))
estatura = float(input("ingrese su estatura en metros: "))
imc = peso/((estatura)**2)

if imc < 18.5:
    print(f"tu indice de masa corporal es: {imc}")
    print("estas bajo de peso")
elif imc >18.4 and imc <24.9:
    print(f"tu indice de masa corporal es: {imc}")
    print("tu peso es normal")
elif imc > 24.9 and imc <29.9:
    print(f"tu indice de masa corporal es: {imc}")
    print("estas en sobrepeso")
else:
    print(f"tu indice de masa corporal es: {imc}")
    print("estas obeso")

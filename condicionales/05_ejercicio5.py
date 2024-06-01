"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
edad = int(input("ingrese su edad: "))
if edad>=16:
    ingreso_mensual = int(input("ingrese sus ingresos mensuales: "))
    if ingreso_mensual>=1000:
        print("usted tiene que tributar")
    else:
        print("su ingreso mensual es menor a lo establecido para poder tributar")
else:
    print("su edad no le permite tributar")
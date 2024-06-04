"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""
edad = int(input("ingrese su edad: "))
#controlar que la edad ingresada no sea menor a 0 y tampoco sea cualquier otro caracter
if edad > 0:
    if edad < 4:
        print(f"su edad es {edad}, puede ingresar gratis")
    elif edad < 18:
        print(f"su edad es {edad}, debe abonar $5 el valor de la entrada")
    else:
        print(f"su edad es {edad}, debe abonar $10 el valor de la entrada")
else:
    print("error, la edad debe de ser mayor a 0 y no puede ser alfanumerica")
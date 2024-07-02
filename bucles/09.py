"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
"""
caracteristicas de los numeros primos
-1 son divisibles por 1 y ellos mismos
-2 al dividirlos dan numeros pares
"""

numero = input("ingrese un numero entero positivo y mayor que 0: ")

#verificar que el numero solicitado sea un entero, y no sea negativo4
while (numero.isdigit() == False) or int(numero)==0:
    print("error. el numero no es entero positivo o es 0")
    numero = input("ingrese un numero entero positivo y mayor que 0: ")

#casteo a entero
numero = int(numero)

#verificar cuantas veces pudo ser dividido, y dio resto 0
cont = 0
for i in range(2,numero):
    if (numero%i) == 0:
        cont+=1 

#verificar si el numero es primo
if cont < 1:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

#nota 1:
#utilizamos la funcion isdigit() esta nos devolvera true si la cadena de texto contiene solo numeros, y false si la cadena contiene espacios o caracteres especiales, como los . en los numeros float

#nota 2:
#sabiendo que los numeros primos solo son divisibles 2 veces(por si mismos y por 1) buscaremos verificar en un rango desde 2 hasta el numero ingresado, cuantas veces pudo ser dividido con resto 0
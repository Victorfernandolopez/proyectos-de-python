"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
#pedir datos
edad = int(input("ingrese su edad: "))

#ciclo for
for i in range(1,edad+1):
    print(i)

#ciclo while
i = 1
while i < edad+1:
    print(i)
    i+=1
"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
#solicita una frase
frase = input("Introduce una frase: ")
#solicita una vocal
vocal = input("Introduce una vocal en minúscula: ")
#reemplaza la vocal de la frace opr la vocal en mayusculas
frase = frase.replace(vocal, vocal.upper())
print(frase)
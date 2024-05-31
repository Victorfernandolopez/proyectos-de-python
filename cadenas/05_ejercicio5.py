"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
#pedido de frase al usuario
frase = input("Introduce una frase: ")
#invertir frase
frase_invertida = frase[::-1]
#mostrar frase invertida
print(frase_invertida)
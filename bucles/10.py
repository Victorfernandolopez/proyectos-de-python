"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
palabra = input("ingrese una palabra: ")

#recorrer la palabra o frase de emezando por el final
for i in palabra[::-1]:
    print(i)

#nota 1
#al iterar sobre la palabra i va a ir tomando el valor de cada uno de los indices que componen la palabra, y al agregar [::-1] esto hahce lo mismo pero a la inverza
#[::-1] == [start : end : pasos ]
#esto hace referencia que el primer parametro indica el comienzo en el que se empiza a leer la cadena, este puede ser desde el comienzo por ezo no tiene nada, pero tambiense puede espesificar si queremos que empieze de cualquier otro caracter.
#el segundo parametro detiene la lectura en el incdice correspondiente
#y el tercero es el que controla los pasos. de un caracter a un caracter, de dos en dos etc. y al agregar el signo "-", esto hace que lo aga de atras para adelante
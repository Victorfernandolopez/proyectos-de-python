"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nombre_completo = input("Introduce tu nombre completo: ")
print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title()) # title() convierte la primer letra de cada palabra de la cadena en mayuscula

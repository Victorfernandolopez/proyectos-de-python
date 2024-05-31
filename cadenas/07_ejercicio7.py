"""
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
correo = input("Introduce tu correo electrónico: ")

# Obtener la parte antes del arroba (@)
nombre = correo.split("@")[0]

# Reconstruir el nuevo correo con el dominio ceu.es
nuevo_correo = f"{nombre}@ceu.es"

# Mostrar el nuevo correo
print(nuevo_correo)
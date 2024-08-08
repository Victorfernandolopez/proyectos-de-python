"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
info = {}
#creamos una lista con los nombres de los campos que desamos que el usuario complete
campos = ['nombre','edad','sexo','telefono']

#llenamos el diccionarios con los datos del usuario
for campo in campos:
    info[campo] = input(f"ingrese su {campo}: ")
    print(info)

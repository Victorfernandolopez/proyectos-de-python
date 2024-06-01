"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
contracena_almacenada = input("ingrese una contraseña: ").lower()
contracena = input("ingrese su contraseña: ").lower()
if contracena_almacenada == contracena:
    print("contraseña correcta")
else:
    print("contraseña incorecta")
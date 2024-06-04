"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
#grupo a= mujeres con nombres antes de la m y los hombre con un nombre posterior a la n
#grupo b= el resto
nombre = input("ingrese su nombre: ").lower()
sexo = input("ingrese su sexo m/f: ").lower()
if (sexo == "m") or (sexo == "f"):
    if sexo == "m":
        if nombre < "m":
            print(f"{nombre} pertenece al grupo (A)")
        else:
            print(f"{nombre} pertenece al grupo (b)")
    elif sexo == "f":
        if nombre > "n":
            print(f"{nombre} pertenece al grupo (A)")
        else:
            print(f"{nombre} pertenece al grupo (b)")
        
else:
    print("error. ingreso un caracter no valido masculino (m) y femenino (f)")

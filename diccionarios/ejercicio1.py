"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
diccionario = {'euro':'€', 'dollar':'$', 'yen':'¥'}

while True:
    divisa = input("ingrese una divisa (Euro,Dollar,Yen): ").lower()
    if divisa in diccionario:
        print(f"El símbolo de {divisa} es {diccionario[divisa]}")
        break   
    else:
        print("no se encontro la divisa. porfavor intente denuevo")
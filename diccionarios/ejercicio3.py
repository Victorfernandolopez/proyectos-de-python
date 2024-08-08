"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""
tabla_frutas = {'platano':1.35,'manzana':0.80, 'pera': 0.85, 'naranja': 0.70}
while True:
    fruta = input("ingrese el nombre de la fruta: ").lower()
    if fruta in tabla_frutas:
        while True:
            kilos = input("ingrese los kilos: ")
            #nota
            if kilos.isdigit() and int(kilos) > 0:
                kilos = int(kilos)
                precio = kilos * tabla_frutas[fruta]
                print(f"el precio por {kilos} kilos de {fruta} es: {precio:.2f}")
                break
            else:
                print("ingrese un numero valido.")
        break
    else:
        print("la fruta no se encuentra en la tabla. intente denuevo.") 
"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""
traductor = {}
# Pedir al usuario las palabras y sus traducciones
while True:
    opcion = input("¿Quiere ingresar una palabra y traducirla (si/no)?: ").lower()
    if opcion == 'si':
        palabra = input("Ingrese la palabra: ")
        traduccion = input("Ingrese su traducción: ")
        traductor[palabra] = traduccion
    elif opcion == 'no':
        if not traductor:
            break
        frase = input("Ingrese una frase para traducirla: ")
        # Traducir frase
        for clave, valor in traductor.items():
            # Reemplazar cada palabra de la frase si está en el diccionario
            frase = frase.replace(clave, valor)
        # Imprimir frase traducida
        print("Frase traducida:", frase)
        break
    else:
        print("Ingrese una opción válida.")
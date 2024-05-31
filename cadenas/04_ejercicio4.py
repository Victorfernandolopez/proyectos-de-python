"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

telefono = input("Ingrese su número con el siguiente formato prefijo-número-extensión (xx-xxxxxxxxx-xx): ")

# Verificar que el número de teléfono tenga la longitud esperada (13 caracteres)
if len(telefono) == 13:
    # Extraer el número sin el prefijo y la extensión
    numero = telefono[2:11]
    print(f"El número de teléfono sin el prefijo y la extensión es: {numero}")
else:
    print("El formato del número de teléfono es incorrecto.")
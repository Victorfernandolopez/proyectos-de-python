"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
# Solicitar al usuario una frase
frase = input("Ingrese una frase: ")

# Solicitar al usuario la letra a contar, asegurándose de que solo ingrese un carácter
letra = input("Ingrese la letra a contar (solo un carácter): ")
while len(letra) != 1:
    letra = input("Por favor, ingrese solo un carácter: ")

# Inicializar el contador en 0
contador = 0

# Recorrer cada caracter en la frase
for caracter in frase:
    # Si el caracter es igual a la letra, incrementar el contador
    if caracter == letra:
        contador += 1

# Mostrar el resultado al usuario
print(f"La letra '{letra}' aparece {contador} veces en la frase.")
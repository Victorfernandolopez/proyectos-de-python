"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
#primer caso
#puedo tomar el valor ingresado directamente como una cadena y separarla con un split() y obtener por un lado el numero de euros y por el otro el numero de centimos

precio = input("ingrese el precio del producto en euros con dos decimales: ")
precio_separado = precio.split(".")
print(f"el numero de euros es: {precio_separado[0]}")
print(f"el numero de centimos es: {precio_separado[1]}")

#en el segundo caso si el precio esta almacenado en una variable entera y esta la vamos a segir usando, nos combiene castear el valor en una otra variable

precio = float(input("ingrese el precio del producto en euros con dos decimales: "))
#aqui casteamos la variable original
precio_cast = str(precio)
precio_separado = precio_cast.split(".")
print(f"el numero de euros es: {precio_separado[0]}")
print(f"el numero de centimos es: {precio_separado[1]}")


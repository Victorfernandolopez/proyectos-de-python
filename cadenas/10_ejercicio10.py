"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
# se busca que el usuario introdusca los productos en un solo imput, y que se impriman uno debajo del otro

#solicitamos los productoos
productos = input("ingrese los productos separados por comas: ")
#reemplazamos el caracter "," por un salto de linea "\n"
print(productos.replace(",","\n"))


#otro ejemplo
#utilizamos join()

#solicitamos los productoos
productos = input("ingrese los productos separados por comas: ")
#separamos los productos en una lista o tupla para poder usar el join() 
lista_productos = productos.split(",")
#imprimimos utilizando join()
print("\n" .join(lista_productos))
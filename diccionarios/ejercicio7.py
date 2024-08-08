"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	            …
Total	    Coste
"""

lista_de_compras = {}
#añadir articulos a la lista
while True:
    opcion = input("quiere ingresar un articulo (si/no): ").lower()
    if opcion == 'si':
        articulo = input("ingrese el nombre del articulo: ")
        while True:
            precio = input("ingrese el valor del articulo: ")
            if precio.replace(".","").isdigit() and float(precio) >0:
                precio = float(precio)
                lista_de_compras[articulo] = precio
                break
            else:
                print("ingrese un numero valido")
    elif opcion == 'no':
        break
    else:
        print("ingrese una opcion valida")

#imprimir lista de compras
print(lista_de_compras)
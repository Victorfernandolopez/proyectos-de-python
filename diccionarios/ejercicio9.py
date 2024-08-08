"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

facturas = {}
opcion = -1
suma = 0
suma2 = 0
#comprobar inputs numericos
def comprobacion_numeros(numero):
    if numero.isdigit():
        return True
    else:
        return False

while opcion !=0:
    print("SISTEMA DE GESTION DE FACTURAS")
    print("ingrese la opcion deseada")
    print("0- salir")
    print("1- añadir factura")
    print("2- pagar factura")
    opcion = input("opcion: ")
    if comprobacion_numeros(opcion) and int(opcion) in [0, 1, 2]:
        opcion = int(opcion)
        if opcion == 0:
            print("saliendo... gracias por usar este programa.")
        elif opcion == 1:
            while True:
                numero_factura = input("ingrese el numero de la factura: ")
                if comprobacion_numeros(numero_factura):
                    if numero_factura not in facturas:
                        while True:
                            valor_coste = input("ingrese el valor del coste: ")
                            if comprobacion_numeros(valor_coste):
                                valor_coste=int(valor_coste)
                                facturas[numero_factura] = valor_coste
                                break
                            else:
                                print("ingrese un valor valido.")
                        print(facturas)
                        break
                    else:
                        print("la factura ya existe. intente con otro numero de factura")
                else:
                    print("ERROR. ingrese un numero valido.")
        elif opcion == 2:
            while True:
                opcion = input("desea abonar una factura (si/no): ").lower()
                if opcion == 'si':
                    numero_factura = input("ingrese el numero de la factura a abonar: ")
                    if comprobacion_numeros(numero_factura) and numero_factura in facturas:
                        suma += facturas[numero_factura]
                        del facturas[numero_factura]
                        print(f"total pagado: {suma}")
                    else:
                        print("ERROR. La factura no exixte")
                elif opcion == 'no':
                    break
                else:
                    print("ERROR. opcion invalida, intente denuevo.")
    else:
        print("ERROR, ingrese una opcion valida.")
"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	        Puntuación
Inaceptable	        0.0
Aceptable	        0.4
Meritorio	    0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""

puntuacion = float(input("ingrese su puentuación (0.0 - 0.4 - 0.6 o mas): "))

#niveles
inaceptable = puntuacion * 2.400
aceptable = puntuacion * 2.400
meritorio = puntuacion * 2.400

#clasificacion de la puntuacion + imprecion de la bonificacion por desempeño
if (puntuacion == 0.0) or (puntuacion==0.4) or (puntuacion>=0.6):
    if puntuacion == 0.0:
        print(f"su rendimiento fue inaceptable, recibira ${inaceptable}")
    elif puntuacion == 0.4:
        print(f"su rendimiento fue aceptable, recibira ${aceptable}")
    elif puntuacion >= 0.6:
        print(f"su rendimiento fue meritorio, recibira ${meritorio}")
        
else:
    print("error. puntuacion no reconocida.")
    print("Las puntuaciones admitidas son : 0.0 ,0.4 ,0.6 o superior")

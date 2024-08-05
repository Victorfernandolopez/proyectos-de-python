"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

#asignacion de la lista
asignatura = ["matematicas", "fisica", "quimica", "historia", "lengua"]
#creamos la lista donde se guardaran las notas
notas = []
#con un for recorremos la lisa de asignaturas mientras preguntamos el puntaje sacado en cada materia recorrida y agregamos ese puntaje a la lista de notas
for materia in asignatura:
    puntaje = int(input(f"que puntaje as sacado en {materia}: "))
    notas.append(puntaje)

#eliminamos de la lista las las materias con notas mayores a 4 que son materias aprovadas
#nota: devemos recorrer la lista de modo inverso para evitar tener conflictos al eliminar elementos de la lista
for i in range(len(asignatura)-1,-1,-1):
    if notas[i]>3:
        del asignatura[i]
        del notas[i]

#imprimimos la las materias desaprovadas
print("usted deve de recursar las materias")
print(asignatura)
    
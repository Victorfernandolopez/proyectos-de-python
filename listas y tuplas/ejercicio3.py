"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
#asignacion de la lista
asignatura = ["matematicas", "fisica", "quimica", "historia", "lengua"]
#creamos la lista donde se guardaran las notas
notas = []
#con un for recorremos la lisa de asignaturas mientras preguntamos el puntaje sacado en cada materia recorrida y agregamos ese puntaje a la lista de notas
for materia in asignatura:
    puntaje = int(input(f"que puntaje as sacado en {materia}: "))
    notas.append(puntaje)
#recorremos la las listas de asignatura y notas imprimiendo el mensaje con el nombre de la materia y el valor
#nota: como recorremos 2 listas con el mismo numero de elementos, y a estos accedemos con su indice, lo mas recomendable es utlizar el for para obtener sus indices
for i in range(len(asignatura)):
    print(f"en {asignatura[i]} has sacado {notas[i]}")
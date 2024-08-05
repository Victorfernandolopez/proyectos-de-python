"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""
#crear lista
asignatura = ["matematicas", "fisica", "quimica", "historia", "lengua"]

#imprimir maerias con mensaje
for materia in asignatura:
    print(f"yo estudio {materia}")
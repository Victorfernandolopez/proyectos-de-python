cadena = "hola mundo"
#convertir el primer caracter en mayuscula y el resto en minusculas (devuelve un string)
cadena = cadena.capitalize()
print(cadena)

#contar cuantas veces aparece una cadena (devuelve un entero)
num_apariciones = cadena.count("o")
print(num_apariciones)

#termina en? (devuelve true/false)
termina_en = cadena.endswith("o")
print(termina_en)

#encontrar donde empieza una cadena especifica (devuelve el indice donde empieza la cadena)
indice_inicio = cadena.find("mundo")
print(indice_inicio)

#encontrar una cadena con index, es igual que con find, pero index devuelve una exepcion del tipo valueError si no se encuentra la cadena
#indice_inicio = cadena.index("mundosss")
#print(indice_inicio)

#saber si todos los caracteres son alfanumericos (devuelve true/false)
alfanumerico = cadena.isalnum()
print(alfanumerico) #devuelve false porque no tiene numeros

#saber si todos los caracteres son letras (devuelve true/false)
letras = cadena.isalpha()
print(letras) #devuelve false porque el espacio entre hola y mundo es un caracter especial, no cuenta como letra

#saber si todos los caracteres son numeros (devuelve true/false)
numeros = cadena.isdigit()
print(numeros)

#convertir todo a minusculas
minusculas = cadena.lower()
print(minusculas)

#convertir todo a mayusculas
mayusculas = cadena.upper()
print(mayusculas)

#eliminar caracteres especifico. por defecto elimina los espacios en blanco (solo el la primer coincidencia)
cadena = "   hola mundo"
eliminar_espacio = cadena.strip()
print(eliminar_espacio)

#reemplazar una subcadena por otra
cadena="hola mundo"
reemplazar = cadena.replace("o","O",1) #parametros del replace(letra vieja, letra nueva, cantidad de veces a reemplasar)
print(reemplazar) #se reemplaza la o minuscula por la o mayuscula solo una vez

#dividir una cadena (devuelve una lista con las palabras divididas)
lista = cadena.split()
print(lista)
cadena = "hola/mundo/hola/muno"
lista = cadena.split("/") #divide la cadena por cada "/" que aparesca
print(lista)


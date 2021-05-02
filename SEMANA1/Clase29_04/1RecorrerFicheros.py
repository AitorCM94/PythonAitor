
#Abrimos el fichero -> Nos devuelve un objeto del tipo <class '_io.TextIOWrapper'>
fichero = open(".\\SEMANA1\\Clase29_04\\1Test.txt", "rt")
"""
for posicion in fichero: #Pinta todas las líneas. Podemos tratar el fichero como si fuera una colección.
    print(posicion)
"""
"""
for posicion in fichero: #Pinta el número de carácteres de cada una de las lineas.
    print(len(posicion))
"""

#Uso de la función .read() -> Devuelva todo el contenido del fichero en formato <class 'str'>.
contenido = fichero.read() 
"""
for posicion in contenido: #Pinta todos los caracteres del fichero entero.
    print(posicion)
"""

#Uso de la funcion .readline() -> Lee la línea del cursor, retorna la información como <class 'str'>, y avanza el cursor a la siguinete línea.
linea = fichero.readline() #Si lo ponemos dos veces lee la primera línea y después la segunda.
#print(linea)
#print(len(linea)) #Pinta el número de caracteres de la linea.
"""
for posicion in linea: #Pinta los caracteres de la primera línea.
    print(posicion)
"""
"""
while linea: #Pinta todas las líneas: Mientras linea -> pinta linea -> linea igual a leer linea en fichero ...
    print(linea)
    linea = fichero.readline()
"""

#Uso de la función .readlines() -> Devuelva el contenido del fichero en formato de <class 'list'> -> Cada línea es una posición.
lineas = fichero.readlines()
#print(lineas) #Se muestra la lista completa.
#print(len(lineas)) #Se muestra el número de líneas (posiciones) que contiene la lista.
#print(lineas[4]) #Podemos acceder directamente a la posición de todos los elementos de la lista.
"""
for posicion in lineas: #Pinta cada elemento de la lista (cada línea).
    print(posicion)
"""

fichero.close() #Es importante cerrar el fichero al finalizar de trabajar.
print(f"Fichero cerrado: {fichero.closed}") #Retorna un boolean.
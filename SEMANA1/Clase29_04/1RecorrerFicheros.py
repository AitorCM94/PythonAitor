
#1Abrimos el fichero -> Nos devuelve un objeto del tipo <class '_io.TextIOWrapper'>
fichero = open(".\\SEMANA1\\Clase29_04\\Test.txt", "rt")
"""
for posicion in fichero: #Pinta todas las líneas.
    print(posicion)
"""

#Uso de la función .read() -> Devuelva el contenido del fichero en formato <class 'str'>.
contenido = fichero.read() 
"""
for posicion in contenido: #Pinta todos los caracteres del fichero entero.
    print(posicion)
"""

#Uso de la funcion .readline() -> Devuelve el contenido de una línea en formato <class 'str'>.
linea = fichero.readline()
"""
for posicion in linea: #Pinta los caracteres de la primera línea.
    print(posicion)
"""
"""
while linea: #Pinta todas las líneas: Mientras linea -> pinta linea -> linea igual a leer linea en fichero ...
    print(linea)
    linea = fichero.readline()
"""

#Uso de la función .readlines() -> Devuelva el contenido del fichero en formato de <class 'list'> -> Cada línea es un elemento.
lineas = fichero.readlines()
#print(lineas)
"""
for l in lineas: #Pinta cada elemento de la lista (cada línea).
    print(l)
"""
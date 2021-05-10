import sqlite3 #Módulo/libreria.

#1. CREACIÓN/CONEXIÓN DE LA BASE DE DATOS:
connection = sqlite3.connect('.\\06_BaseDatos\\SQLite.db') #Si el fichero no existe lo crea.
#1.1 Generamos el cursor
cursor = connection.cursor() #Tupla.

#2. CREACIÓN DE LA TABLA:
#2.1 Ver si una tabla existe: Preguntamos a la tabla master (donde se encuentran todos los objetos de la base de datos).
cursor.execute("SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Alumnos'") #Buscar todos los registros cuyo tipo (type) se aigual a tabla (table) y nombre = Alumnos.
tablas = cursor.fetchone()[0] #Con count() nos devuelve una Tupla con el número de tablas.
#2.2 Crear la tabla:
if(tablas == 0): #Si ya ha creado la tabla, tablas será igual al número de tablas coincidentes. Si no hay ninguna, devolverá 0 y crearemos la tabla.
    cursor.execute("CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)") #Ejecutamos.

#3. INSERTAR REGISTROS:
"""
#3.1 Insertar un registro en la base de datos:
cursor.execute("INSERT INTO Alumnos VALUES ('A00', 'Aitor','Cerdán', '2B', Null)") #Comando literal de la base de datos -> Null
connection.commit()
"""
"""
#3.2 Insertar varios registros en la base de datos:
#Creamos la lista: Lista de tuplas, en python el valor Null es None.
listaAlumnos = [('A01', 'Clamaran','Cerdán', '2B', None), ('A02', 'Rotia','Cerdán', '2B', None), ('A03', 'Pepito','Cerdán', '2B', None)]
cursor.executemany("INSERT INTO Alumnos VALUES (?, ?, ?, ?, ?)", listaAlumnos) #Ejecutamos el comando con los comodines y la lista.
connection.commit() #Confirmación de la inserción.
"""

#MANERAS DE CONSULTAR LOS DATOS:

command = "SELECT * FROM Alumnos" #Comando que pide todos los registros (Alumnos LIMIT 2 -> Elegir dos registros) de la tabla alumno, con todos los campos* (columnas).

#Opción 1:
for a in cursor.execute(command): #Ejecutar y recorrer a la vez.
    print(a)
print()

#Opción 2:
cursor.execute(command) #Ejecutamos la sentencia.
for a in cursor.fetchall(): #Con fetchall capturamos en una lista todos los datos del cursor. Los recorremos y pintamos.
    print(a)
print()

#Opción 3:
cursor.execute(command) #Ejecutamos la sentencia.
a = cursor.fetchone() #Con fetchone capturamos y avanzamos el cursor dato por dato.
while (a):
    print(a)
    a = cursor.fetchone()
print()

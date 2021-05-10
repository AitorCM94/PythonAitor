import sqlite3
import pymssql
#1. BASE DE DATOS:
#1.1 Establecemos la conexión con una base de datos en caso de que exista, y si no la creamos:
connection1 = sqlite3.connect('.\\06_BaseDatos\\SQLite_Northwind.db')
#1.2 Generamos el cursor:
cursor1 = connection1.cursor() #Tupla.

#2. TABLA:
#2.1 Ejecutamos un comando para ver si la tabla existe:
cursor1.execute("SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Customers'")
numTablas = cursor1.fetchone()[0] #Retorna una tupla con el número de tablas.
#2.2 Creamos la tabla Customers si no existe: (Con los mimso campos que tiene Customers en SQL Server)
if (numTablas == 0):
    cursor1.execute("CREATE TABLE Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)") #Ejecutamos.

#0. CONEXIÓN CON LA BASE DE DATOS SQL SERVER:
connection2 = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind')
cursor2 = connection2.cursor()

#0.1 Ejecutamos el comando para capturar todos los registros en SQL Server:
cursor2.execute('SELECT * FROM Customers')
listClient = cursor2.fetchall()
#print(listClient)

#3. INSERTAR REGISTROS en SQLite:
cursor1.executemany("INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", listClient) #Insertmany
#3.0 Con un for:
for r in listClient:
    cursor1.execute("INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", listClient)

connection1.commit() #CONFIRMAMOS LA INSERCIÓN.


cursor1.close()
cursor2.close()
connection1.close()
connection2.close()
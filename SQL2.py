import pymssql
import sys

conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind') #Conexión.

cursor = conexion.cursor() #Tupla
r = cursor.execut("INSERT INTO Customers (CustomerID, CompanyName, City, Country) VALUES ('DEMO2', 'Empresa2', 'Madrid', 'Spain')")
conexion.commit() #Gravar en la base de datos.

print(type(r))
print(r)

sys.exit()
import pymssql

#1. Establecemos la conexión:
conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind')
#2. Creamos el objeto cursor:
cursor = conexion.cursor()

#3. Ejecutamos el comando de inserción en Transat-SQL:
cursor.execute("INSERT INTO Customers (CustomerID, CompanyName, City, Country) VALUES ('DEMO', 'Empresa', 'Madrid', 'Spain')") #Entrecomillar con comillas dobles.

#4. Hacer un commit para confirmar la inserción.
conexion.commit()

#INSERCIONES MASIVAS -> Insertar muchos registros de una sola vez:
#1 Comando de inserción masiva en Transat-SQL (+comodines):
comando = "INSERT INTO Customers (CustomerID, CompanyName, City, Country) VALUES (%s, %s, %s, %s)"

#3.2 Creamos la lista con las tuplas() (o diccionarios{}) que contienen los valores que sustituiran los comodines:
lista = []
lista.append(('DEXX1', 'Empresa 1, SL', 'Barcelona', 'Spain'))
lista.append(('DEXX2', 'Empresa 2, SL', 'Barcelona', 'Spain'))
lista.append(('DEXX3', 'Empresa 3, SL', 'Barcelona', 'Spain'))
lista.append(('DEXX4', 'Empresa 4, SL', 'Barcelona', 'Spain')) #Insertamos una Tupla en cada append.

#3. Ejecutamos el comando de inserción masiva:
cursor.executemany(comando, lista)

#4. Hacer un commit para confirmar la inserción.
conexion.commit()


cursor.close() #Cerramos el cursor.
conexion.close() #Cerramos la conexión.
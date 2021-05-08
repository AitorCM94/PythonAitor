import pymssql

#1. Establecemos la conexión:
conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind')
#2. Creamos el objeto cursor:
cursor = conexion.cursor()

#3. Ejecutamos el comando de borrar en Transat-SQL:
cursor.execute("DELETE FROM [Customers] WHERE [CustomerID] = 'DEMO1'")
#Para borrar varios a la vez:
#cursor.executemany("DELETE FROM [Customers] WHERE [CustomerID] = %s", listaID)
#4. Hacer el commit para confirmar el comando:
conexion.commit()

#Para pintar el número de filas afectadas:
print(f"Filas modificadas: {cursor.rowcount}")


cursor.close() #Cerramos el cursor.
conexion.close() #Cerramos la conexión.
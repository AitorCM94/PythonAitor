import pymssql #Librería para conectarnos con SQL Server.

#1. Conexión:
conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind')

#2. Con el objeto conexion CREAMOS UN OBJETO CURSOR que nos permite ejecutar comandos de Transat-SQL:
cursor = conexion.cursor() #Retorna un objeto Cursor. Si queremos trabajar con un dicconario -> (as_dict=True): Usar claves en vez de posiciones.

#3. Ejecutamos la sentencia de consulta (query) sobre el cursor:
cursor.execute('SELECT * FROM Customers') #Selecciona todas las columnas de la tabla Customers -> Sin filtro = todos los registros (filas).

#3. CARGAMOS EL CURSOR: Ejecutamos la función de recuperación de la información:
fila = cursor.fetchone() #Retorna una Tupla donde cada posición es una columna del registro (fila) -> Nos posicionamos en la primera fila.
#Podemos recorrer todos los registros con un WHILE usando el CURSOR y FETCHONE:
while(fila):
    print(f"     ID: {fila[0]}") #Pintamos la columna en la posición 0. Si cambiamos la sentencia de execute cambian las posiciones.
    print(f"Empresa: {fila[1]}") #Con el diccionario: columna['CompanyName']
    print("") #Espacio para diferenciar un registro (fila) de otro.
    fila = cursor.fetchone() #Posiciona cursor en el siguiente registro.

#IMPORTANTE: Solo tenemos un cursor. Cuando tenemos que encadenar búsquedas tenemos que VACIAR antes el cursor:
filas = cursor.fetchall() #Retorna una Lista donde cada posición es una Tupla formada por las columnas de un registro.
#Hemos volcado todos los datos en una lista, de esta manera podemos recorrer la lista con un for y dejar libre el cursor.

cursor.close() #Cerramos el cursor.
conexion.close() #Cerramos la conexión.
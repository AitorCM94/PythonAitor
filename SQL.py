import pymssql

conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind') #Conexión.

cursor = conexion.cursor() #Tupla
#cursor = conexion.cursor(as_dict=True) #Diccionario. Con claves. Podemos ver el dato que estamos pintando.
cursor.execute('SELECT * FROM Customers')

row = cursor.fetchone()
#print(type(row))
#print(row)
while(row):
    print(f"     ID: {row[0]}") #Posicion: en tuplas. No vemos que dato estamos pintando.
    print(f"Empresa: {row[1]}") #Con el diccionario: row['CompanyName']
    print("")
    row = cursor.fetchone()

cursor.close()
conexion.close()
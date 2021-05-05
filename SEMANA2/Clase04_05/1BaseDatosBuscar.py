from pymongo import MongoClient #Es el objeto que representa la conexión a la base de datos.
from pprint import pprint

#--------------Conexión con Base de datos--------------#

#1. Establecer la conexión con MongoDB (motor de base de datos):
client = MongoClient('mongodb://localhost:27017') #Cadena de conexión.
#client = MongoClient('localhost',27017) #Direccion ip o nombre del servidor, puerto.

#2. Ver el estado del servidor (motor de base de datos):
db = client.admin #Asignamos a la variable db el objeto que representa la base de datos (client). Y ejecutamos el comando .admin
#Sobre esta base de datos (db) podremos ejecutar diferentes funciones referente a la base de datos:
status = db.command("serverStatus") #.command permite ejecutar comandos. "serverStatus" pinta el estado del servidor.
#pprint(status) #Con pprint() pintamos los datos de una manera más manejable.

#--------------Acceder a las colecciones--------------#

#1. Seleccionar la base de datos:
northwindDB = client.Northwind #Volcamos en la variable: [motor de base de datos].[nombre de la base de datos] -> Notación de objeto.
#northwindDB = client['Northwind'] #También podemos tratar las B.D. como si fueran claves de un diccionario -> Notación de diccionario.

#2. Listar las colecciones de la base de datos:
print(northwindDB.list_collection_names()) #Nos devuelve una lista string -> Podemos recorrerla con un for -> Podemos usar filter(len()) para buscar las colecciones...
#print(northwindDB.list_collections()) #Nos devuelve una lista de objetos coleccion.

#3. Seleccionar una colección de la base de datos:
collection = northwindDB.customers #Variable que contiene la base de datos. El nombre de la colección' -> Notación de objeto.
#collection = northwindDB['customers'] #Notación de diccionario.

#Sin la variable que contiene la base de datos:
#collection = client.Northwind.customers #Variable que contiene el motor de la B.D. La base de datos. La colección. -> Notación de objeto.
#collection = client['Northwind']['customers'] #Notación de diccionario.

#--------------Trabajar con los documentos--------------# -> Métodos:
#1. Contar documentos:
result = collection.estimated_document_count()

#2. BUSCAR documentos:
#result = collection.find_one() #Devuelve el primer elemento coincidente.

#result = collection.find() #Devuelve un objeto Cursor de tipo colección que podemos recorrer:
#for document in result:
#    pprint(document) #Pinta todos los documentos de la colección.

#2.1 Añadir el FILTRO de búsqueda:
#result = collection.find_one({'CustomerID': 'LAUGB'}) #La {'clave':'valor'} es un objeto. Por eso va entre {}

result = collection.find({'Country': 'USA'}) #Devuelve una colección con todos los elementos encontrados (claves) -> Podemos recorrerlo:
while (result.alive): #.alive devuelve un boolean True si quedan más elementos o False si el cursor ya se encuentra en el último.
    pprint(result.next()) #El método next hace que pinte las claves. Posiciona el cursor en el siguiente elemento.
result.close() #Cerrar el cursor.

result = collection.find({'Country': 'USA', 'City': 'Portland'}) #Buscar dos campos concretos.
result = collection.find({'Country': {'$in' : ['USA', 'Mexico']}}) #Buscar dos valores en un mismo campo. $in -> valor contenido en la colección especificada[].

#2.2 Pintar el número de elementos encontrados:
print("Número de documentos: ", collection.count_documents({'Country': 'USA'})) #La base de datos nos dice cuantos hay (datos no descargados).
#print("Número de documentos: ", result.count()) #Nos dice el número de elementos de la búsqueda (datos descargados).

print("Datos por leer: ", result.alive)

#2.3 Otros:
result = collection.find({'Country': 'USA'}).sort('City') #Ordenar los resultados directamente en la base de datos: (datos no descargados)
result = collection.find({'Country': 'USA'}).limit(5) #Limitar la búsqueda a X documentos.
result = collection.find({'Country': 'USA'}).skip(5) #Desechar los X primeros registros (útil cuando leemos de manera paginada)
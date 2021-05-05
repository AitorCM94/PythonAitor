from pymongo import MongoClient #Es el objeto que representa la conexión a la base de datos.

#--------------CONEXIÓN CON BASE DE DATOS--------------#

#1. Establecer la conexión con MongoDB (motor de base de datos):
client = MongoClient('mongodb://localhost:27017') #Cadena de conexión.
#client = MongoClient('localhost',27017) #Direccion ip o nombre del servidor, puerto.

#1.1. Ver el estado del servidor (motor de base de datos):
db = client.admin #Asignamos a la variable db el objeto que representa la base de datos (client). Y ejecutamos el comando .admin
#Sobre esta base de datos (db) podremos ejecutar diferentes funciones referente a la base de datos:
status = db.command("serverStatus") #.command permite ejecutar comandos. "serverStatus" pinta el estado del servidor.
#pprint(status) #Con pprint() pintamos los datos de una manera más manejable.

#2. Seleccionar la base de datos:
northwindDB = client.Northwind #Volcamos en la variable: [motor de base de datos].[nombre de la base de datos] -> Notación de objeto.
#northwindDB = client['Northwind'] #También podemos tratar las B.D. como si fueran claves de un diccionario -> Notación de diccionario.

#--------------ACCEDER A LAS COLECCIONES--------------#

#0. Listar las colecciones de la base de datos:
print(northwindDB.list_collection_names()) #Nos devuelve una lista string -> Podemos recorrerla con un for -> Podemos usar filter(len()) para buscar las colecciones...
#print(northwindDB.list_collections()) #Nos devuelve una lista de objetos coleccion.

#1. Seleccionar una colección de la base de datos:
collection = northwindDB.customers #Variable que contiene la base de datos. El nombre de la colección' -> Notación de objeto.
#collection = northwindDB['customers'] #Notación de diccionario.

#Sin la variable que contiene la base de datos:
#collection = client.Northwind.customers #Variable que contiene el motor de la B.D. La base de datos. La colección. -> Notación de objeto.
#collection = client['Northwind']['customers'] #Notación de diccionario.

#--------------DOCUMENTOS--------------#
#Contar documentos:
result = collection.estimated_document_count()
print(result)

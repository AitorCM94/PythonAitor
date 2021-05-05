from pymongo import MongoClient #Es el objeto que representa la conexión a la base de datos.
from pprint import pprint

#--------------Conexión con Base de datos--------------#

#1. Establecer la conexión con MongoDB (motor de base de datos):
client = MongoClient('mongodb://localhost:27017') #Cadena de conexión.
db = client.admin #Asignamos a la variable db el objeto que representa la base de datos (client). Y ejecutamos el comando .admin

#--------------Acceder a las colecciones--------------#
#1. Seleccionar la base de datos:
northwindDB = client.Northwind #Volcamos en la variable: [motor de base de datos].[nombre de la base de datos] -> Notación de objeto.
#2. Listar las colecciones de la base de datos:
northwindDB.list_collection_names() #Nos devuelve una lista string -> Podemos recorrerla con un for -> Podemos usar filter(len()) para buscar las colecciones...
#3. Seleccionar una colección de la base de datos:
collection = northwindDB.customers #Variable que contiene la base de datos. El nombre de la colección' -> Notación de objeto.

#--------------Trabajar con los documentos--------------# -> Métodos:
#1. Contar documentos:
result = collection.estimated_document_count()

#2. BUSCAR documentos:
#result = collection.find_one({'CustomerID': 'LAUGB'}) #Devuelve el primer elemento coincidente.
#result = collection.find({'Country': 'USA', 'City': 'Portland'}) #Devuelve un objeto Cursor de tipo colección que podemos recorrer:
#for document in result:
#    pprint(document) #Pinta todos los documentos de la colección.

#2.2 Pintar el número de elementos encontrados:
print("Número de documentos: ", collection.count_documents({'Country': 'USA'}))
#print("Datos por leer: ", result.alive)

#2.3 Otros:
result = collection.find({'Country': 'USA'}).sort('City') #Ordenar los resultados directamente en la base de datos: (datos no descargados)
result = collection.find({'Country': 'USA'}).limit(5) #Limitar la búsqueda a X documentos.
result = collection.find({'Country': 'USA'}).skip(5) #Desechar los X primeros registros (útil cuando leemos de manera paginada)

#3. Insertar datos:
#Creamos una estructura (variable) que represente el documento y nos permita ir añadiendo valores:
customer = {
    "CustomerID": "DEMO1",
    "CompanyName": "EuroTomb, SL",
    "ContactName": "Aitor Cerdán Mañé",
    "ContactTitle": "Propietario",
    "Address": "Calle del bombo",
    "City": "Barcino",
    "Region": "Hispania",
    "PostalCode": "00001",
    "Country": "Spain",
    "Phone": "(91) 200 20 20",
    "Fax": "(91) 200 80 80"
} #Objeto expresado con conotación de JavaScript. Las llaves simpre representan un objeto.

#idNewDocument = collection.insert_one(customer).inserted_id #Para insertar un documento. Añade un identificador.

#4. Modificar un documento:
query = {'CustomerID': 'DEMO1'} #Definir la consulta -> query
newValues = {
    "$set": {
    "CompanyName": "blablabla", 
    "ContactTitle": "blablabla"
    }
} #Valores que quiera modificar. Todos los que queramos.
#result = collection.update_one(query, newValues) #La instrucción para actualizarlo (solo uno, el primero).
#print(result.matched_count, 'elementos encontrados')
#print(result.modified_count, 'elementos modificados')
#pprint(collection.find_one(query)) #Nos pinta el elemento actualizado.


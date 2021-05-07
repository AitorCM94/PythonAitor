from pymongo import MongoClient
from pprint import pprint #Permite usar la función pprint() para pintar datos da manera más interpretable. (“pretty-print”).
from bson.objectid import ObjectId #Usar funciones o atributos para buscar por el identificador.

#CLIENTE:
client = MongoClient('mongodb://localhost:27017')
#BASE DE DATOS:
northwindDB = client.Northwind
#COLECCIONES:
collection = northwindDB.customers

#--------------FUNCIONES--------------#

result = collection.find_one() #Devuelve el primer elemento coincidente.

result = collection.find() #Devuelve un objeto Cursor de tipo colección que podemos recorrer:
#for document in result:
#    pprint(document) #Pinta todos los documentos de la colección.

#--------------AÑADIR FILTROS--------------#

result = collection.find_one({'CustomerID': 'LAUGB'}) #La {'clave':'valor'} -> Propiedad de un obejto {}.

result = collection.find({'Country': 'Mexico'}) #Devuelve un tipo de colección Cursor con todos los documentos que coinciden con la clave -> Podemos recorrerlo:
while (result.alive): # .alive devuelve True si quedan más documentos por recorrer -> Es decir si podemos seguir ejecutando el .next()
    pprint(result.next()) #.next() posiciona el cursor en el siguiente documento.
result.close() #Cerrar el cursor.

#BUSCAR DOS CAMPOS CONCRETOS:
result = collection.find({'Country': 'USA', 'City': 'Portland'})
#BUSCAR DOS VALORES EN UN MISMO CAMPO:
result = collection.find({'Country': {'$in' : ['USA', 'Mexico']}}) # $in -> valor contenido en la colección especificada[].
#BUSCAR POR EL ObjectID:
result = collection.find_one({'_id' : ObjectId('60927747c76c96f538b0fa64')})

#--------------CONTAR NÚMERO DOCUMENTOS--------------#

print("Número de documentos filtrados: ", collection.count_documents({'Country': 'USA'})) #La base de datos nos dice cuantos hay (datos no descargados).
print("Número de documentos totales: ", collection.estimated_document_count())
##print("Número de documentos: ", result.count()) #Nos dice el número de elementos de la búsqueda (datos descargados).

#print("Datos por leer: ", result.alive)

#--------------FUNCIONES DE BÚSQUEDA AVANZADA--------------#

result = collection.find({'Country': 'USA'}).limit(5) #Limitar la búsqueda a X documentos.
result = collection.find({'Country': 'USA'}).skip(5) #Desechar los X primeros registros (útil cuando leemos de manera paginada)
result = collection.find({'Country': 'USA'}).sort('City') #Ordenar los resultados ('City') directamente en la base de datos: (datos no descargados)
result = collection.find({'Country': 'USA'}).sort('City', 1) #Ordenar las ciudades de manera ascendente (-1 descendente). Podemos recorrerlo:
#for d in result:
#    pprint(d)

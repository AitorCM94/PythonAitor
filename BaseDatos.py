from pymongo import MongoClient #Objeto cliente que nos permite la conexión con la base de datos.
from pprint import pprint

#Establecer conexión con MongoDB (motor de base de datos):
#Pasar direccion ip o nombre del servidor:
client = MongoClient('mongodb://localhost:27017')
#client = MongoClient('localhost',27017)

#Estado del servidor (motor de base de datos):
db = client.admin #volcar sobre la variable un objeto que representa la base de datos admin.
status = db.command("serverStatus") #.command permite ejecutar comandos. Pintamos el estado del servidor (toda la información del servidor).
#print(status) #Datos inmanegables
#pprint(status) #Pintamos los datos con pprint -> más manejable.


##Trabajando con Datos:
#Seleccionar la base de datos:
northwindDB = client.Northwind #Volcar la base de datos (nombre de la base de datos) en la variable. Notación de objeto.
#northwindDB = client['Nortwind'] #Lo mismo. Lo trata como una clave. Notación de diccionario.

#Listar las colecciones de la base de datos. Recorrerlas para acceder a los datos.
#print(northwindDB.list_collections()) #Lista de objetos.
print(northwindDB.list_collection_names()) #Lista string. Podemos recorrerlas con el for.
#Con un filter, si nos devuelve 0 eementos no existe, si devuelve uno si. Más eficiente, preguntar si un alfanumerico se encuentra dentro de la lista.

#Seleccionar una coleccion de la base de datos.
#Diferentes fórmulas: 
#collection = northwindDB['customers'] #Notación de diccionario. Nombre de la colección.
#collection = northwindDB.customers #con notacion de objeo. Igual que seleccionar la base de datos.
#Siempre con la variable que contiene la base de datos. Si no:
collection = client.Northwind.customers 
#collection = client['Northwind']['customers']

#Uso de métodos para acceder a la colección: 
result = collection.estimated_document_count() #Para contar el número de registros (documentos).
#print(result)

#BÚSQUEDA de documentos:
#result = collection.find_one() #Primer elemento coincidente.
result = collection.find({'Country': 'USA'}, {'Country': 'Mexico'}).sort('City') #Todos los elementos coincidentes. Devuelve una coleccion que podemos recorrer.

#print("Número de documentos: ", result.count())
print("Número de documentos: ", collection.count_documents({'Country': 'USA'}))
print("Datos por leer: ", result.alive)
#for d in result: #Recorremos todos los registros encontrados
#    pprint(d)
while (result.alive == True):
    pprint(result.next())

#El filtro de busquedo lo pasamos como un objeto dentro de la función .find({objeto}) sobre el elemento que queremos que realize búsqiedas
#El metodo .next() pinta el usuario. Posiciona el cursor en el siguiente registro.
# .alive -> Para ver las propiedades del cursor. Muy interesante para recorrer los registros con un while -> Siempre que devuelva true podemos ejecutar el nex.

#Es micho más eficiente contar los elementos en las bases de datos. Funciones que hagan calculos en las bases de datos en vez de en local.
# .sort('[elementos]') ordenar los elementos.


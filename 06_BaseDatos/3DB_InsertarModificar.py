from pymongo import MongoClient
from pprint import pprint
import json #Para utilizar funciones y propiedades referentes al formato json.

#CLIENTE:
client = MongoClient('mongodb://localhost:27017')
#BASE DE DATOS:
northwindDB = client.Northwind
#COLECCIONES:
collection = northwindDB.customers

#--------------INSERTAR UN DOCUMENTO (JSON)--------------#

#1. Dentro de una variable creamos una estructura que represente el documento y nos permita ir añadiendo valores:
customer = {
    "CustomerID": "DEMO3",
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
} #Variable que contiene un objeto expresado con conotación de JavaScript (entre llaves = objeto).

#2. Usamos la funcion:
#idNewDocument = collection.insert_one(customer).inserted_id #Para insertar un documento. Añade un identificador.

#--------------MODIFICAR DOCUMENTOS--------------#

#1. Creamos las variables:
query = {'CustomerID': 'DEMO3'} #Definir la consulta (query) -> Determina los documentos a modificar.
newValues = {
    "$set": { #Comando set -> Se utiliza para asignar valores a las propiedades
    "CompanyName": "blablabla", 
    "ContactTitle": "blablabla"
    }
} #Claves y Valores a modificar. Todos los que queramos.

#2. Usamos las funciones:
#result = collection.update_one(query, newValues) #La instrucción para actualizarlo (solo uno, el primero).
#result = collection.update_many(quert, newValues) #Para modificar todos los registros con la clave coincidente.

#2.1 Comprovamos:
#print(result.matched_count, 'elementos encontrados')
#print(result.modified_count, 'elementos modificados')
#pprint(result)
#pprint(collection.find_one(query)) #Nos pinta el elemento actualizado.

#--------------INSERTAR UN DOCUMENTO (Python)--------------# 

#1. Creamos la clase:
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None

#2. Instanciamos el objeto y le añadimos valores:
cliente = Customer()
cliente.CustomerID = "DEMO2"
cliente.CompanyName = "EuroTomb, SL"
cliente.ContactName = "Aitor Cerdán Mañé"
cliente.ContactTitle = "Propietario"
cliente.Address = "Calle del bombo"
cliente.City = "Barcino"
cliente.Region = "Hispania"
cliente.PostalCode = "00001"
cliente.Country = "Spain"
cliente.Phone = "(91) 200 20 20"
cliente.Fax = "(91) 200 80 80"

#3. Pasar el objeto cliente a JSON: 
pprint(cliente.__dict__) #__dict__ -> Devuelve las propiedades en formato JSON.
#Si quisiéramos hacer nosotros la conversión deberíamos hacer una función que seleccione los parámetros a convertir. O:
#pprint(json.dumps(cliente, default=lambda x: x.__dict__)) #Uso de la función .dumps, el objeto y el encoder (cuna función lambda). Devuelve una Tupla (no funciona).

#4. Usamos la función:
#idNewDocument = client.Northwind.customers.insert_one(cliente.__dict__).inserted_id #Añadir el documento.

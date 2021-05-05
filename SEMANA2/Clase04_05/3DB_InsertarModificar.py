from pymongo import MongoClient
from pprint import pprint

#CLIENTE:
client = MongoClient('mongodb://localhost:27017')
#BASE DE DATOS:
northwindDB = client.Northwind
#COLECCIONES:
collection = northwindDB.customers

#--------------INSERTAR DATOS JSON--------------#

#Creamos una estructura (variable) que represente el documento y nos permita ir añadiendo valores:
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
} #Objeto expresado con conotación de JavaScript. Las llaves simpre representan un objeto.

#idNewDocument = collection.insert_one(customer).inserted_id #Para insertar un documento. Añade un identificador.

#--------------MODIFICAR UN DOCUMENTO--------------#

query = {'CustomerID': 'DEMO3'} #Definir la consulta -> query
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

########################################################### -> Insertar con python como objeto. -> 05/05/2021
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
#-------------------------#
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

#2. Convertir el objeto cliente en JSON: #No es posible convertir el objeto directamente en JSON.
#pprint(cliente.__dict__)

#idNewDocument = client.Northwind.customers.insert_one(cliente.__dict__).inserted_id #Añadir el documento.

###########################################################

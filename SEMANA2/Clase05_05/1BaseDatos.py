from pymongo import MongoClient
from pprint import pprint
import sys, json #Funciones de sistema.

#CLIENTE:
client = MongoClient('mongodb://localhost:27017')
#BASE DE DATOS:
northwindDB = client.Northwind
#COLECCIONES:
collection = northwindDB.customers

#--------------AGREGACIONES--------------#

c = client.Northwind.customers.find_one()
o = client.Northwind.orders.find_one()

data = client.Northwind.customers.aggregate([
    {'$match' : {'CustomerID' : 'ANATR'}},
    {'$sort' : {'City' : 1}},
    {'$lookup' : {
        'from' : 'orders',
        'localField' : 'CustomerID',
        'foreignField' : 'CustomerID', #En ambos documentos coincide el nombre CustomerID.
        'as' : 'Orders' #Nombre de la nueva clave.
        }
    } #Consulta múltiple entre dos colecciones.
])
datos = data.next()
print('ID:', datos['CustomerID'])

sys.exit() #Finaliza el programa
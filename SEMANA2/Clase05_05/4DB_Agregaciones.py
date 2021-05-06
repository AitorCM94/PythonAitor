from pymongo import MongoClient
from pprint import pprint
import sys #Funciones de sistema.

#CLIENTE:
client = MongoClient('mongodb://localhost:27017')
#BASE DE DATOS:
northwindDB = client.Northwind
#COLECCIONES:
customers = northwindDB.customers
orders = northwindDB.orders
#En la base de datos todos los pedidos (orders) tienen el identificador del cliente al que pertenece el pedido.

#--------------AGREGACIONES--------------#
#0. Buscar la información del cliente y de los pedidos:
c = customers.find_one({'CustomerID':'ANATR'})
o = orders.find_one({'CustomerID':'ANATR'})

#1. Mostrar los datos de ANATR y la lista de todos sus pedidos: (búsqueda de manera conjunta -> AGREGACIÓN):
data = customers.aggregate([
    {'$match' : {'CustomerID' : 'ANATR'}}, #Búsqueda del cliente -> comando $match
    {'$sort' : {'City' : 1}}, #Lo ordenamos por ciudad (en este caso indiferente).
    #La operación de capturar en la misma sentencia los pedidos de ANATR:
    {'$lookup' : {
        'from' : 'orders', #Colección donde vamos a buscar (la que queremos mezclar).
        'localField' : 'CustomerID', #Elemento (clave) que relciona ambas colecciones.
        'foreignField' : 'CustomerID', #En ambos documentos coincide el nombre de la clave que los relaciona.
        'as' : 'Orders' #Nombre de una nueva clave que contendrá los pedidos (orders).
        } #Es una lista.
    } 
]) #Consulta múltiple entre dos colecciones. Devuelve un diccionario.
datos = data.next() #.next() es un cursor para cargar el siguiente elemento de la lista. .alive nos dice si es true podemos seguir ejecutando el .next()
#pprint(datos)

#2. Pintar los datos:
print('ID:', datos['CustomerID'])
print('Empresa:', datos['CompanyName'])
print('País:', datos['Country'])
#Para los pedidos:
for o in datos['Orders']: #Nombre que le hemos dado a la nueva clave.
    print('ID Pedido: ', o['OrderID'])
    print('ID Empleado: ', o['EmployeeID'])

#sys.exit() #Finaliza el programa
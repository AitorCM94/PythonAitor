from itertools import product
from pymongo import MongoClient
#Cliente:
client = MongoClient('mongodb://localhost:27017/')
#Base de datos:
db = client.Northwind
#Colecciones:
orders = db.orders
deatils = db.order_details
products = db.products


idPedido = input('Identificador del Pedido: ')
pedido = orders.find_one({'OrderID' : idPedido})
if(pedido != None):
    print(f"Entregar:   {pedido['ShipName']}")
    print(f"            {idPedido['ShipAddress']}")
    print(f"            {idPedido['ShipCity']} ({idPedido['ShipCountry']})")
    print(f"")
    #Buscamos el detalle del pedido:
    detalle = details.find({'OrderID' : idPedido})
    #Recorrer con un while el cursor del detalle del pedido:
    while(detalle.alive):
        linea = detalle.next()
        #Buscamos y mostramos la descricpción del producto, utilizando ProductID:
        producto = products.find_one({'ProductID' : linea['ProductID']})
        #Mostramos cada línea de pedido:
        total = int(linea['Quantity']) * float(linea['UnitPrice'])
        print(f"{producto['ProductName']} {linea['Quantity']} {linea['UnitPrice']} {total}")
    
    #Mostramos el importe total del pedido.

else:
    print(f"El pedido {idPedido} no existe.")
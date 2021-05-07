from itertools import product
from pymongo import MongoClient

#Motor de la base de datos:
client = MongoClient('mongodb://localhost:27017/')
#Base de datos:
db = client.Northwind

##EJERCICIO: EXTRAER INFORMACIÓN / RECORRER INFORMACIÓN / MOSTRAR INFORMACIÓN.

#COLECCIONES QUE VAMOS A USAR:
orders = db.orders
details = db.order_details
products = db.products
#Introducir el ID de un pedido (en products) y mostrar el detalle del pedido (en details). 
# Buscamos los detalles (productos y precios) del pedido -> Con el mismo ID en la colección details:

#1. Pedimos el ID del pedido:
idPedido = input('Identificador del Pedido: ') 

#2. Buscamos si el ID del pedido coincide con algún documento de la colección orders:
pedido = orders.find_one({'OrderID' : idPedido}) #Buscamos un objeto (nos devuelve None si no existe).
if(pedido != None): #Si el pedido existe. 
#2.1 Pintamos los datos del pedido -> En la colección orders:
    print(f"==============================================================")
    print(f"  DATOS DEL PEDIDO {idPedido}")
    print(f"==============================================================")
    print(f"Entregar:   {pedido['ShipName']}")
    print(f"            {pedido['ShipAddress']}")
    print(f"            {pedido['ShipCity']} ({pedido['ShipCountry']})")
    print(f"")
    #Pintamos la cabezera de los detalles del pedido:
    print(f"==============================================================")
    print(f"  {'Producto':<31} {'Cant. '} {'Precio':>10} {'Total':>10}")
    print(f"==============================================================")
#3. Buscamos si el ID del pedido coincide con algún documento de la colección details: (buscamos los detalles del pedido: Cantidades y precio unidad)
    detalles = details.find({'OrderID' : idPedido}) #Devuelve un objeto Cursor (una lista) con los documentos coincidentes.
#4. Recorremos los documentos del objeto Cursor (detalles):
    totalPedido = 0
    while(detalles.alive): #Mientras queden documentos por recorrer.
        DocDet = detalles.next() #Posiciona el cursor en el siguiente documento.
        #5. Calculamos el precio de todas las cantidades:
        precioProd = int(DocDet['Quantity']) * float(DocDet['UnitPrice'])
        precioProdF = "{:1.2f}".format(precioProd) #Formateamos el número.
        #6. Buscamos el nombre del producto -> En la colección products (con el ID):
        producto = products.find_one({'ProductID' : DocDet['ProductID']})
        #7. Calculamos el precio total del pedido:
        totalPedido += precioProd
        totalPedidoF = "{:1.2f}".format(totalPedido)
        #Pintamos las claves del producto (documento):
        print(f"  {producto['ProductName']:<31} {DocDet['Quantity']:>6} {DocDet['UnitPrice']:>10} {precioProdF:>10}") 
        #Tabula la información: Especificar el máximo de espacios de la columna y su alineación (<izquierda, >derecha)
    #Pintamos el importe total del pedido:
    print(f"==============================================================")
    print(f"  {'TOTAL':>49} {totalPedidoF:>10}")    
else:
    print(f"El pedido {idPedido} no existe.")

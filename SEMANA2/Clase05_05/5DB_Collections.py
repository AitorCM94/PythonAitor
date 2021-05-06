from itertools import product
from pymongo import MongoClient

#Cliente:
client = MongoClient('mongodb://localhost:27017/')

#Base de datos:
db = client.Northwind

#Colecciones:
orders = db.orders
details = db.order_details
products = db.products


#Ejercicio: Introducir el ID de un pedido (products) y mostrar el detalle del pedido (details): EXTRAER INFORMACIÓN/RECORRER INFORMACIÓN/MOSTRAR INFORMACIÓN.

idPedido = input('Identificador del Pedido: ') #Input del id del pedido.

pedido = orders.find_one({'OrderID' : idPedido}) #Búsqueda del pedido con el id.
if(pedido != None): #Si el pedido existe. Lo pintamos:
    print(f"=================================================================")
    print(f"  DATOS DEL PEDIDO {idPedido}")
    print(f"=================================================================")
    print(f"Entregar:   {pedido['ShipName']}")
    print(f"            {pedido['ShipAddress']}")
    print(f"            {pedido['ShipCity']} ({pedido['ShipCountry']})")
    print(f"")
    #Buscamos el detalle del pedido:
    detalle = details.find({'OrderID' : idPedido}) #Devuelve un cursor que tendremos que recorrer con While:
    print(f"=================================================================")
    print(f"  {'Producto':<35} {'Cant. '} {'Precio'} ")
    print(f"=================================================================")
    while(detalle.alive): #.alive nos dice si es true podemos seguir ejecutando el .next()
        #Buscamos la información del producto:
        linea = detalle.next() #Recorrmos cada línea de la colección de detalles del pedido.
        producto = products.find_one({'ProductID' : linea['ProductID']}) #Buscamos en la colección de products (con el ID) el nombre, para pintarlo.
        totalLinea = int(linea['Quantity']) * float(linea['UnitPrice']) #Calculamos el dinero total del pedido.
        #Pintamos la información obtenida:
        print(f"  {producto['ProductName']:<35} {linea['Quantity']:>6} {linea['UnitPrice']:>8} {totalLinea:>8}") 
        #Tabula la información: Especificar el máximo de espacios de la columna y su alineación (<izquierda, >derecha)
    #Mostramos el importe total de todos los pedidos.
    #importeTotal = 
    #print(f"Importe total: {}")
else:
    print(f"El pedido {idPedido} no existe.")
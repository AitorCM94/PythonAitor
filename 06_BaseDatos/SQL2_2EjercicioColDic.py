import pymssql
import sys

conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind') #Conexión.

#1. Pedimos el ID del pedido:
idPedido = input('Identificador del pedido: ') 

#2. Buscamos si el ID del pedido coincide con algún registro de la tabla Orders:
cursor = conexion.cursor(as_dict=True) #CREAMOS EL OBJETO CURSOR -> PASAMOS LA TUPLA A DICCIONARIO.
cursor.execute('SELECT ShipName, ShipAddress, ShipCity, ShipCountry FROM Orders WHERE OrderID = %s', idPedido) #Ejecutamos el comando de búsqueda.

#Sentencia de control para determinar si el pedido existe o no:
if(cursor.rowcount == 0): 
    print(f"El pedido {idPedido} no existe.")
else:
#3. Pintamos las columnas de la fila encontrada:
    fila = cursor.fetchone() #CARGAMOS EL CURSOR -> Diccionario. //1 elemento -> Vacío=True
    print(f"==============================================================")
    print(f"  DATOS DEL PEDIDO {idPedido}")
    print(f"==============================================================")
    print(f"Entregar:   {fila['ShipName']}")
    print(f"            {fila['ShipAddress']}")
    print(f"            {fila['ShipCity']} ({fila['ShipCountry']})")
    print(f"")

    print(f"==============================================================")
    print(f"  {'Producto':<31} {'Cant. '} {'Precio':>10} {'Total':>10}")
    print(f"==============================================================")

#4. Buscamos los detalles del pedido:
    cursor.execute('SELECT Quantity, UnitPrice, ProductID FROM [Order Details] WHERE OrderID = %s', idPedido) #Ejecutamos el comando de búsqueda.
    lista = cursor.fetchall() # VOLVEMOS A CARGAR EL CURSOR -> Lista que contiene diccionarios. //1 elemento -> Vacío=True

#5. Pintamos detalles de los pedidos, contenidos en los diccionarios, contenidos en la lista:
    totalPedidos = 0
    for diccionario in lista: #Recorremos todos los diccionarios en lista.
        total = diccionario['Quantity'] * diccionario['UnitPrice'] #Calculamos el precio total de cada diccionario.
        #5.1 Buscamos el nombre del producto en otra tabla (Products):
        cursor.execute('SELECT ProductName FROM Products WHERE ProductID = %s', diccionario['ProductID']) #Que coincida con el ProductID
        producto = cursor.fetchone() #VOLVEMOS A CARGAR EL CURSOR -> Diccionario. //1 elemento -> Vacío=True
        #5.2 Calculamos el precio de todos los pedidos:
        totalPedidos += total #Sumamos el total de cada diccionario.
        totalPedidosF = "{:1.2f}".format(totalPedidos) #Formateo.
        #5.3. Pintamos todos los datos:
        print(f"  {producto['ProductName']:<31} {diccionario['Quantity']:>6} {diccionario['UnitPrice']:>10} {total:>10}")
    print(f"==============================================================")
    print(f"  {'TOTAL':>49} {totalPedidosF:>10}")

cursor.close() #Cerramos el cursor.
conexion.close() #Cerramos la conexión.
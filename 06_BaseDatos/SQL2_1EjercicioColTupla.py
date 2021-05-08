#from itertools import product #?
import pymssql
import sys

conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind') #Conexión.

#1. Pedimos el ID del pedido:
idPedido = input('Identificador del pedido: ') 

#2. Buscamos si el ID del pedido coincide con algún registro de la tabla Orders:
cursor = conexion.cursor() #CREAMOS EL OBJETO CURSOR.
cursor.execute('SELECT * FROM Orders WHERE OrderID = %s', idPedido) #Ejecutamos el comando de búsqueda.

#Sentencia de control para determinar si el pedido existe o no:
if(cursor.rowcount == 0): #rowcount -> Si da 0 es que no hay datos. Si da -1 es que hay datos.
    print(f"El pedido {idPedido} no existe.")
else:
#3. Pintamos las columnas de la fila encontrada:
    fila = cursor.fetchone() #CARGAMOS EL CURSOR -> Tupla. //1 elemento -> Vacío=True
    print(f"==============================================================")
    print(f"  DATOS DEL PEDIDO {idPedido}")
    print(f"==============================================================")
    print(f"Entregar:   {fila[8]}")
    print(f"            {fila[9]}")
    print(f"            {fila[10]} ({fila[13]})")
    print(f"")

    print(f"==============================================================")
    print(f"  {'Producto':<31} {'Cant. '} {'Precio':>10} {'Total':>10}")
    print(f"==============================================================")

#4. Buscamos los detalles del pedido:
    cursor.execute('SELECT * FROM [Order Details] WHERE OrderID = %s', idPedido) #Ejecutamos el comando de búsqueda.
    lista = cursor.fetchall() # VOLVEMOS A CARGAR EL CURSOR -> Lista que contiene tuplas. //1 elemento -> Vacío=True

#5. Pintamos detalles de los pedidos, contenidos en las tuplas, contenidas en la lista:
    totalPedidos = 0
    for tupla in lista: #Recorremos todas las tuplas en lista.
        total = tupla[3] * tupla[2] #Calculamos el precio total de cada tupla.
        #5.1 Buscamos el nombre del producto en otra tabla (Products):
        cursor.execute('SELECT ProductName FROM Products WHERE ProductID = %s', tupla[1]) #Que coincida con el ProductID
        producto = cursor.fetchone() #VOLVEMOS A CARGAR EL CURSOR -> Tupla. //1 elemento -> Vacío=True
        #5.2 Calculamos el precio de todos los pedidos:
        totalPedidos += total #Sumamos el total de cada tupla.
        totalPedidosF = "{:1.2f}".format(totalPedidos) #Formateo.
        #5.3. Pintamos todos los datos:
        print(f"  {producto[0]:<31} {tupla[3]:>6} {tupla[2]:>10} {total:>10}")
    print(f"==============================================================")
    print(f"  {'TOTAL':>49} {totalPedidosF:>10}")

cursor.close() #Cerramos el cursor.
conexion.close() #Cerramos la conexión.
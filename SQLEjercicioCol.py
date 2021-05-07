#from itertools import product #?
import pymssql
import sys

conexion = pymssql.connect(server='localhost', user='Aitor', password='Carapato88', database= 'Northwind') #Conexión.

#1. Pedimos el ID del pedido:
idPedido = input('Identificador del Pedido: ') 

#2. Buscamos si el ID del pedido coincide con algún registro de la tabla orders:
cursor = conexion.cursor() #Tupla -> as_dict=true
cursor.execute('SELECT * FROM Orders WHERE OrderID = %s', idPedido) #Class none type
#print(r) #None



row = cursor.fetchone() #Class tuple
print(f"==============================================================")
print(f"  DATOS DEL PEDIDO {idPedido}")
print(f"==============================================================")
print(f"Entregar:   {row[8]}")
print(f"            {row[9]}")
print(f"            {row[10]} ({row[13]})")
print(f"")


cursor.execute('SELECT * FROM [Order Details] WHERE OrderID = %s', idPedido)
lista = cursor.fetchall()
for l in lista:
    total = l[3] * l[2]
    cursor.execute('SELECT ProductName FROM Products WHERE ProductID = %s', l[1])
    producto = cursor.fetchone()
    print(f"  {producto[0]:<31} {l[3]:>6} {l[2]:>10} {total:>10}")


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

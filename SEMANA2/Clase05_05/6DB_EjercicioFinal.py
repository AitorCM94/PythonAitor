from pymongo import MongoClient

#Cliente:
connect = MongoClient('mongodb://localhost:27017/')

#Base de datos:
db = connect.Northwind

#Colecciones:
orders = db.orders
details = db.order_details
products = db.products


##Buscar cuantos productos tenemos:
#print("Número de productos: ", products.estimated_document_count())

##Buscar y mostrar todos los productos:
listProducts = products.find() #Devuelve un objeto Cursor de tipo colección (como si fuera una lista) que podemos recorrer:
#for document in listProducts:
#    print(f"{document['ProductName']}") #Pinta todos los documentos de la colección.
#Con un while:
#cursor = products.find()
#while(cursor.alive): #Cuando .live is true.
#    print(cursor.next()['ProductName'])

##Buscar productos con UnitsInStock = 0:
#pro = list(filter(lambda p: p['UnitsInStock'] == '0', listProducts)) #Buscar los productos de manera local.
#for p in pro:
#    print(f"{p['ProductName']}")
#pNoStock = products.find({'UnitsInStock': '0'}) #Buscar los productos en la base de datos. Más optimizado.
#for document in pNoStock:
#    print(document['ProductName'])

##Coste o Valor de nuestro Stock - Producto -> UnitsInStock, UnitPrice:
pInStock = products.find({'UnitsInStock':{'$ne':'0'}}) #Buscamos los productos que tienen stock no igual a 0.
valorStock = 0
for p in listProducts:
    valorStock += (float(p['UnitPrice']) * float(p['UnitsInStock']))

print(f"\nValor del Stock: {valorStock:1.2f}")

##Con la función de agregación podemos hacer que la base de datos nos de directamente la operación... POR MIRAR!!!
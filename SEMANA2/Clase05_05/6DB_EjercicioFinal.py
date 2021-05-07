from pymongo import MongoClient

#Cliente:
connect = MongoClient('mongodb://localhost:27017/')
#Base de datos:
db = connect.Northwind
#Colecciones:
products = db.products


##1. CONTAR NÚMERO DE DOCUMENTOS (productos):
#print("Número de productos: ", products.estimated_document_count())

##2. BUSCAR Y MOSTRAR TODOS LOS DOCUMENTOS (productos):
listProducts = products.find() #Devuelve un objeto Cursor de tipo colección (como si fuera una lista) que podemos recorrer:
#for document in listProducts:
#    print(f"{document['ProductName']}") #Document es un diccionario -> Entre [] la clave para acceder a su valor.
cursor = products.find()
while(cursor.alive): #Cuando .live is true.
    print(cursor.next()['ProductName']) #Cursor es un diccionario.

##3. BUSCAR DOCUMENTOS CON LA CLAVE UnitsInStock = 0:
listProducts = products.find()
ListNoStock = list(filter(lambda p: p['UnitsInStock'] == '0', listProducts)) #Buscar los productos de manera local. Retorna una lista. 
#for p in ListNoStock:
#    print(f"{p['ProductName']}")
CurNoStock = products.find({'UnitsInStock': '0'}) #Buscar los productos en la base de datos -> Más optimizado. Retorna un Cursor.
#for document in CurNoStock:
#    print(document['ProductName'])

##4. SUMAR VALORES (precio del stock) -> CLAVES (UnitsInStock / UnitPrice):
pInStock = products.find({'UnitsInStock':{'$ne':'0'}}) #Buscamos los productos que tienen stock NO igual a 0.
valorStock = 0
for p in pInStock:
    valorStock += (float(p['UnitPrice']) * float(p['UnitsInStock']))

print(f"\nValor del Stock: {valorStock:1.2f}")
"""
#4.1 Utilizando las funciones map() y sum ():
TotalStock = sum(list(map(lambda x: float(x['UnitPrice']) * float(x['UnitsInStock']) ,productos.find())))
print(f"\nValor del Stock: {TotalStock:1.2f}")

##4.2 CON LA FUNCIÓN DE AGREGACIÓN -> Podemos hacer que la base de datos nos de directamente la operación:
query = [
    { '$match': { 'UnitsInStock' : { '$ne': '0' } } },
    { '$addFields': {
        'Price': { '$toDouble': '$UnitPrice' },
        'Stock': { '$toInt': '$UnitsInStock' },
        }
    },
    { '$group': {
        '_id': 'Valor del Stock', 
        'Total': { '$sum': { '$multiply': [ '$Price', '$Stock' ] } },
        'Items': { '$sum' : 1 }
        }
    }      
]

listProductos = productos.aggregate(query)
print(listProductos.next())
"""
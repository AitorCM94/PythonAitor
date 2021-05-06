
from pymongo import MongoClient

#Cliente:
connect = MongoClient('mongodb://localhost:27017/')

#Base de datos:
db = connect.Northwind

#Colecciones:
productos = db.products


# Coste o Valor de nuestro Stock utilizand map() y sum()
TotalStock = sum(list(map(lambda x: float(x['UnitPrice']) * float(n['UnitsInStock']) ,productos.find())))
print(f"\nValor del Stock: {TotalStock:1.2f}")
print("")

# Coste o Valor de nuestro Stock utilizando la función aggregate()
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
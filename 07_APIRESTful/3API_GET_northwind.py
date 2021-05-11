import requests

url = 'http://api.labs.com.es/v1.0/clientes.ashx' #Esta URL funciona con parámetros (params).

#1. Creamos un diccionario para los parámetros:
inID = input("ID: ")
paramsCliente = {'id' : inID} #Su valor es el input.
#Opción2:
#paramsCliente = {} #Diccionario vacío.
#paramsCliente['id'] = inID #Añadimos valor al diccionario.

#2. Incluimos en la petición get la url + los parámetros:
response = requests.get(url, params=paramsCliente)

#3. Pintamos los datos recibidos: (Lista)
if (response.status_code == 200):
    if('application/json' in response.headers['Content-Type'].split(';')): #Cabecera -> Content-Type con más de un valor separado por ';' -> Lista.
        data = response.json()

        if(len(data) > 0): #Si los elementos de la coleccion són mayor que 0 -> Es decir que el ID existe.
            for d in data: #Con el for recorremos la lista y pintamos cada uno de sus elementos.
                print(f"{d['CustomerID']:>14}# {d['CompanyName']}")
                print(f"{'Contacto: ':>15} {d['ContactName']} ({d['ContactTitle']})")
                print(f"{'Dirección: ':>15} {d['Address']}")
                print(f"{'':>15} {d['PostalCode']} {d['City']}")
                print(f"{'':>15} {d['Country']}")
                print(f"{'Tel/Fax: ':>15} {d['Phone']} {d['Fax']}")
                print("")
                #data[0]['CompanyName'] #Sin el for -> pintamos cada posicion, en este caso: [0]
        else: #Si no existe el id.
            print(f"El identificador {inID} no pertenece a ningún cliente.")

    else:
        print("No se puede procesar el contenido.")
else:
    print('Error: ', response.reason)

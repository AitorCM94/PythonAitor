import requests

#1. Llamada al microservicio:
#Variables
url = 'http://www.zippopotam.us/es/' #IMPORTANTE LA BARRA DEL FINAL!!
CodPost = input("Código postal: ")
#Llamada/respuesta:
response = requests.get(url + CodPost) #Modo get.

#2. Pintamos los datos recibidos:
if (response.status_code == 200):
    if(response.headers['Content-Type'] == 'application/json'):
        data = response.json() #Serializamos la respuesta -> Nos permite pintar el contenido como un diccionario.
        for d in data['places']: #Recorremos cada posición de la lista, y ejecutamos el bloque por cada posición.
            print('Ciudad: ', d['place name'])
            print(f"Provincia: {d['state']} ({d['state abbreviation']})")
            print(f"País: {data['country']} ({data['country abbreviation']})") #Esta información está fuera de 'places'.
            print(f"Longitud: {d['longitude']} / Latitud: {d['latitude']}")
            print("")
    else:
        print("Formato no compatible.")
else:
    print('Error: ', response.reason)

#LISTA: data['places'] -> Posición [0] de la lista (me da un diccionario) -> Clave del diccionario ['place name']
#print(data['places'][0]['place name']) #Lista + posición (dando por sentado que solo devolverá una lista con una posición[0]), y luego cada uno de los datos.

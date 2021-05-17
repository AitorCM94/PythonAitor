import requests
"""
#from termcolor import colored, cprint

#Borja -> Definición de la función para utilizarla con el map():
def ParkingInfo(item):
    data = {} #Construimos un diccionario con cada uno de los datos:
    data['id'] = item['id']
    data['name'] = item['name']
    data['adress'] = item['adress']

    if(item['freeParking'] == None): #Transforma el "Null" en no disponible.
        data['freeParking'] = 'no disponible'
    else:
        data['freeParking'] = f'{item["freeParking"]:1.0f}'

    return data
"""
#=============================================================================#
url = {
    'Login': 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'Parking': 'https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability/'
}
#1. LOGIN -> AUTENTICACIÓN PARA ACCEDER A LOS END-POINTS DE LA API:
headers = {'X-ClientId': '000bf007-bae7-431b-8afa-b69003ef7633', 'passKey': '38EE7DF56F54937A55E938C3A0B634FBDB06C1485E7877976E79891A0A4DCE758D0BAF53B59F2FB388035A9E1C99A493FE814D1A19A4171E11CB0BAFF15A77E6'}
token = None

response = requests.get(url['Login'], headers=headers)
if(response.status_code == 200):
    token = response.json()['data'][0]['accessToken']
    headers = {'accessToken': token}
#2. CONEXIÓN CON LA URL DEL PARKING:
    responseParking = requests.get(url['Parking'], headers=headers)
    if (response.status_code == 200):
        """ #NO VA -> KeyError: 'id'
        data = list(map(ParkingInfo, response.json()['data'])) #El map retorna una colección con el id, el nombre y la dirección; y si hay plazas o no.
        #Para buscar el número de plazas totales:
        freeParkingTotal = sum( #Suma de la lista con el número de plazas.
            list(map(lambda x: x['freeParking'], #2.Me quedo con el número de las plazas. -> Lista con el número de plazas.
                list(filter(lambda y: y['freeParking'] != None, response.json()['data']))))) #1.Filter para quitar los "Null" (None) -> Lista solo con los que tienen datos.
        #Pintamos:
        for item in data:
            plazas = colored(f"{item['freeParking']}", "red")

            print(f"{item['name']:<30} Plazas: {plazas}")
            print(f"{item['address']}")
            print()
        """
        #Aitor:
        data = responseParking.json()
        total = 0
        for d in data['data']:
            if (d['freeParking'] != None):
                print(f"{d['name']}: {d['freeParking']}")
                #print(type(d['freeParking']))
                total += d['freeParking']
        print(f"Plazas totales: {total}")

    #print('Código de Estado: ', responseParking.status_code)
    #print('Estado: ', responseParking.reason)
    #print(responseParking.text)
else:
    print('Error: ', response.reason)

import requests
from requests.models import to_key_val_list
from datetime import datetime
import json
"""
#2.3.2 Borja -> Definición de la función
def InfoBus(item):
    #1. Creamos un diccionario con los cuatro datos:
    data = {}
    #Añado el número de línea:
    data['line'] = item['line'] 
    #Añado el tiempo en llegar:
    if(item['estimateArrive'] < 60): #Si el tiempo estimado es menor de 60 segundos.
        data['time'] = 'está en la parada'
    else: #Si no:
        time = item['estimateArrive'] / 60 #Obtenemos los minutos.
        if(time >= 20): #Más de 20 min.
            data['time'] = 'llegará en 20 min o más'
        else: #Tiempo estimado entre medias.
            data['time'] = f'llegará aproximadamente en {time:1.0f} min.'
    #Añado la distancia:
    data['distance'] = item['DistanceBus'] 
    #Añado el mensaje:
    data['message'] = f'el {data["line"]} {data["time"]} ({data["distance"]} m.)' 
"""
#=============================================================================#
#0. Probar que tenemos conectividad con el API:
#url = "https://openapi.emtmadrid.es/v1/hello/"
#response = requests.get(url)
#print(response.text) 
#print(response.json()['message']) #Lo pasamos a JSOn y pintamos la clave.

url = {
    'Login': 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'Stops': 'https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopId>/arrives/'
}

#1. LOGIN -> AUTENTICACIÓN PARA ACCEDER A LOS END-POINTS DE LA API:
headers = {'X-ClientId': '000bf007-bae7-431b-8afa-b69003ef7633', 'passKey': '38EE7DF56F54937A55E938C3A0B634FBDB06C1485E7877976E79891A0A4DCE758D0BAF53B59F2FB388035A9E1C99A493FE814D1A19A4171E11CB0BAFF15A77E6'}
token = None

response = requests.get(url['Login'], headers=headers) #Dentro de la respuesta obtenemos el TOKEN.
#print(response.text)
if(response.status_code == 200):
    token = response.json()['data'][0]['accessToken'] #TOKEN -> Cadena alfanumérica que nos autoriza el acceso a los end-points.
    #print('token: ', response.json()['data'][0]['accessToken'])
else:
    print("Error: ", response.reason)

#2. CONEXIÓN CON EL END POINT PARA VER EL TIEMPO DE LOS AUTOBUSES:
if(token != None):
#2.1 Componentes necesarios para hacer la llamada:
    parada = input("Parada: ")
    headers = {'accessToken': token} #EN LA CABECERA MANDAMOS SIEMPRE EL TOKEN DE ACCESO.
    data = {
        "cultureInfo":"ES",
        "Text_StopRequired_YN":"Y",
        "Text_EstimationsRequired_YN":"Y",
        "Text_IncidencesRequired_YN":"Y",
        "DateTime_Referenced_Incidencies_YYYYMMDD": datetime.now().date().strftime('%Y%m%d')
    } #Esto es un diccionario -> Tenemos que convertirlo en JSON (json.dumps(data))
#2.2 LLAMADA -> POST
    responseStops = requests.post(url['Stops'].replace('<stopId>', parada), headers=headers, data=json.dumps(data)) #.replace() para sustituir la palabra indicada por la input parada.
#2.3 Extraer la información y pintarla:
    
    #2.3.1 David:
    data = responseStops.json()
    arrives = data['data'][0]['Arrive']

    print(f"Información de la parada {parada}")

    for arrive in arrives:
        print("===========================================")
        print(f"Línea: {arrive['line']}.")
        print(f"{'':>5}- Destino: {arrive['destination']}.")
        print(f"{'':>5}- Distancia: {arrive['DistanceBus']}.")

        minutos = arrive['estimateArrive'] // 60

        if (minutos < 2):
            if minutos == 0:
                minutos = "Llegando"
            else:
                minutos = f'{minutos} minuto'
        else:
            if(minutos > 20):
                minutos = '+20 minutos'
            else:
                minutos = f'{minutos} minutos'
        print(f"{'':>5}- Tiempo estimado de llegada: {minutos}.")
    """
    #2.3.2 Borja:
    if(response.status_code == 200): #NO FUNCIONA -> KeyError: 'Arrive'
        data = list(map(InfoBus, response.json()['data'][0]['data'])) #response.json -> Datos como parámetros de Infobus -> Función de map().

        for item in data:
            print(f"{item['message']}")
    
    else:
        print("Error: ", response.reason)
    """
    """
    #Extracción v1 de los datos:
    print(data['code'])
    print(data['description'])
    print(data['datetime'])
    for d in data['data']:
        print(d['Arrive'][0]['line'])
        print(d['Arrive'][0]['stop'])
        print(d['Arrive'][0]['destination'])
        print(d['Arrive'][0]['geometry']['type'])
        print(d['Arrive'][0]['geometry']['coordinates'][0])
        print(d['Arrive'][0]['geometry']['coordinates'][1])
        print((d['Arrive'][0]['estimateArrive']) / 60)
        print(d['Arrive'][0]['DistanceBus'])
    """
else:
    print("Error: ", response.reason)


#print('Código de Estado: ', responseStops.status_code)
#print('Estado: ', responseStops.reason)
#print(responseStops.text)


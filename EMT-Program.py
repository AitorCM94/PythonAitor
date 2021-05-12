import requests
from requests.models import to_key_val_list
import json
#Probar que tenemos conectividad con el api:
#response = requests.get(url)
#print(response.text) 
#print(response.json()['message'])

url = {
    #'Base': 'https://openapi.emtmadrid.es/v1/',
    'Login': 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'Stops': 'https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/'
}

headers = {'X-ClientId': '000bf007-bae7-431b-8afa-b69003ef7633', 'passKey': '38EE7DF56F54937A55E938C3A0B634FBDB06C1485E7877976E79891A0A4DCE758D0BAF53B59F2FB388035A9E1C99A493FE814D1A19A4171E11CB0BAFF15A77E6'}
token = None
parada = input("Parada: ")

response = requests.get(url['Login'], headers=headers)
if(response.status_code == 200):
    #print(response.text)
    token = response.json()['data'][0]['accessToken']
    #print('token: ', response.json()['data'][0]['accessToken'])
    headers = {'accessToken': token}
    data = {
        "cultureInfo":"ES",
        "Text_StopRequired_YN":"Y",
        "Text_EstimationsRequired_YN":"Y",
        "Text_IncidencesRequired_YN":"Y",
        "DateTime_Referenced_Incidencies_YYYYMMDD":"20210512"
    }
    #POST
    responseStops = requests.post(url['Stops'] + parada + "/arrives/", headers=headers, data=json.dumps(data))
    data = responseStops.json()
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
    
    #print('Código de Estado: ', responseStops.status_code)
    #print('Estado: ', responseStops.reason)
    #print(responseStops.text)
else:
    print('Error: ', response.reason)





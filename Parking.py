import requests
import json

#Plazas libres -> freeParking //Parking name.
url = {
    #'Base': 'https://openapi.emtmadrid.es/v1/',
    'Login': 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'Parking': 'https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability/'
}

headers = {'X-ClientId': '000bf007-bae7-431b-8afa-b69003ef7633', 'passKey': '38EE7DF56F54937A55E938C3A0B634FBDB06C1485E7877976E79891A0A4DCE758D0BAF53B59F2FB388035A9E1C99A493FE814D1A19A4171E11CB0BAFF15A77E6'}
token = None

response = requests.get(url['Login'], headers=headers)
if(response.status_code == 200):
    #print(response.text)
    token = response.json()['data'][0]['accessToken']
    #print('token: ', response.json()['data'][0]['accessToken'])
    headers = {'accessToken': token}
    
    responseParking = requests.get(url['Parking'], headers=headers)
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

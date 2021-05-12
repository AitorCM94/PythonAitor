import requests

#CREACIÓN DE REGISTROS (POST):

#1.Construcción de la llamada:
url = "http://postman-echo.com/post/"
#Diccionarios para cada una de la información a enviar:
params1 = {'param1':'demo', 'param2':'demo'}
headers1 = {'content-type':'application/json'}
data1 = {'Nombre':'Aitor', 'Apellidos':'Cerdán'}
#Llamada al microservicio en modo POST:
response = requests.post(url, data=data1, params=params1, headers=headers1)

#2. Comprobamos que la llamada se ha realizado correctamente:
print('Código de Estado: ', response.status_code) #Código de estado -> 200
print('Estado: ', response.reason) #Código de estado en formato texto.
print()

#3. Pintamos las cabeceras y el contenido:
if (response.status_code == 200):
    print('Cabeceras: ', response.headers)
    print()
    print('Contenido: ', response.text)
else:
    print('Error: ', response.reason)

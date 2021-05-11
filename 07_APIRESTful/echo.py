import requests

#LLAMADA A MICROSERVICIO:
url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url) #Llamadas en modo GET. Retorna un objeto de tipo Response.

#CÓDIGOS DE ESTADO:
print('Código de Estado: ', response.status_code) #Código de estado -> 200
print('Estado: ', response.reason) #Código de estado en formato texto.

#Pintar cabeceras y contenido:
if (response.status_code == 200):
    print('Cabeceras: ', response.headers) #Cabecera -> Información.
    print('Tipo del contenido: ', response.headers['Content-Type']) #Formato de la aplicación.
    if(response.headers['Content-Type'] == 'application/json'):
        data = response.json() #Lo convertimos en json -> Nos permite pintar el contenido como en un diccionario.
        print('JSON: ', response.json()) 
        print('Latitud: ', data['iss_position']['latitude'])
        print('Longitud: ', data['iss_position']['longitude'])
        print('Timestamp: ', data['timestamp'])
        print('Mensaje: ', data['message'])
    else:
        print('Contenido: ', response.text) #Contenido en formato texto.
        print('Contenido: ', response.content) #Contenido en bytes.
else:
    print('Error: ', response.reason)

print("======================POST======================")

#Utilizamos la función post() para realizar llamadas a microservicios en modo POST -> Creación de registros.
url = "http://postman-echo.com/post"

#Construcción de diccionarios:
params1 = {'param1':'demo', 'param2':'demo'}
headers1 = {'content-type':'application/json'}
data1 = {'Nombre':'Aitor', 'Apellidos':'Cerdán'}

response = requests.post(url, data=data1, params=params1, headers=headers1)

print('Código de Estado: ', response.status_code) #Código de estado -> 200
print('Estado: ', response.reason) #Código de estado en formato texto.

if (response.status_code == 200):
    print('Cabeceras: ', response.headers) #Cabecera -> Información.
    print('Contenido: ', response.text) #Contenido en formato texto.
    #print('Contenido: ', response.content) #Contenido en bytes.
else:
    print('Error: ', response.reason)

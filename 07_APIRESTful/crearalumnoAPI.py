#Get -> Devuelve los alumnos.
#Post -> Creación de un alumno.

import requests
from requests.api import head
from requests.models import Response
import json

url = "http://school.labs.com.es/api/students"

#Preguntar el alta, clase id 1, 2, 3, construimos los datos, llamada del alumno.
nombre = input("Nombre: ")
apellido = input("Apellido: ")
fechaNacimiento = input("Fecha de nacimiento: ")
clase = int(input("Clase(1, 2, 3): "))

header = {'content-type':'application/json'}
data = {'firstName':nombre, 'lastName':apellido, 'dateOfBirth':fechaNacimiento, 'classId':clase}

response = requests.post(url, headers=header, data=json.dumps(data)) #json.dumps(data) #Para convertir diccionario data en json.

#print('Código de Estado: ', response.status_code)
#print('Estado: ', response.reason)

if(response.status_code == 201):
    print('Alumno: ', response.json()['id'])
else:
    print("Error: ", response.reason)

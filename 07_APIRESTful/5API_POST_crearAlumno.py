import requests
import json

#CREACIÓN DE REGISTROS (POST):

#1.Construcción de la llamada:
url = "http://school.labs.com.es/api/students/" #Get -> Devuelve los alumnos // Post -> Crear alumno.
#1.1 Preguntas con los datos para el nuevo alumno:
nombre = input("Nombre: ")
apellido = input("Apellido: ")
fechaNacimiento = input("Fecha de nacimiento: ") #Modo texto.
clase = int(input("Clase(1, 2, 3): "))
#1.2 Diccionarios para incorporar los datos a la llamada:
header = {'content-type':'application/json'}
data = {'firstName':nombre, 'lastName':apellido, 'dateOfBirth':fechaNacimiento, 'classId':clase}
#1.3 Llamada en modo post:
response = requests.post(url, headers=header, data=json.dumps(data)) #json.dumps(data) -> Para convertir el texto de data en json = Diccionario.

#2. Comprobamos que la llamada se ha realizado correctamente:
print('Código de Estado: ', response.status_code)
print('Estado: ', response.reason)

#En la respuesta tenemos el objeto del alumno creado (en JSON) con un 'id' asignado.

#3. Pintamos el ID del alumno:
if(response.status_code == 201): #Código 201 -> Creado.
    print('ID alumno: ', response.json()['id'])
else:
    print("Error: ", response.reason)

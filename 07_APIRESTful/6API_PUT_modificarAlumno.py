import requests
import json
#GET -> Consultar el alumno por el identificador:
#1. Construcción de la llamada:
url = 'http://school.labs.com.es/api/students/'
idAlumno = input("ID Alumno: ")
data = None #Variable para los datos del alumno.
#1.1 Llamada en modo get con el input id:
response = requests.get(url + idAlumno)
#1.2 Comprobamos que la llamada se ha realizado correctamente:
print('Código de Estado: ', response.status_code)
print('Estado: ', response.reason)

#2. Pintamos los datos:
if (response.status_code == 200):
    data = response.json() #Convierto la respuesta para obtener el diccionario.
    
    for key in data.keys(): #Para pintar cada una de las propiedades (claves -> .keys()) del diccionario.
        if(key == 'id'): #Para que no pinte de nuevo el ID.
            continue
        print(f"{key}: {data[key]}")

else:
    print('Error: ', response.reason)


#MODIFICAR LOS DATOS -> PUT:
#1. Preguntamos por los nuevos datos asignandolos a sus claves:
nombre = input(f"Nombre ({data['firstName']}): ")
apellido = input(f"Apellido ({data['lastName']}: ")

#2. Incorporación de los nuevos valores al diccionario alumno:
if(nombre != ''):
    data['firstName'] = nombre

if(apellido != ''):
    data['lastName'] = apellido

#3. Llamada en modo put para hacer la modificación:
respones = requests.put(url + idAlumno, data=json.dumps(data)) ##Necesitamos de nuevo la URL con el 'id', Convertir a json.


#print('Código de Estado: ', response.status_code)
#print('Estado: ', response.reason)

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

#BORRADO
conf = input("Borrar Alumno: ")

if(conf == "si"):
    respones = requests.delete(url + idAlumno)

    print('Código de Estado: ', response.status_code)
    print('Estado: ', response.reason)
else:
    print("ok")
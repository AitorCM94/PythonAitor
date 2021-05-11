import requests
import json

url = 'http://school.labs.com.es/api/students/'
idAlumno = input("ID Alumno: ")
data = None

response = requests.get(url + idAlumno)

#print('Código de Estado: ', response.status_code)
#print('Estado: ', response.reason)

if (response.status_code == 200):
    data = response.json() #Lo convertimos en json -> Nos permite pintar el contenido como en un diccionario.
    
    for key in data.keys():
        if(key == 'id'): #Para que no pinte de nuevo el ID.
            continue
        print(f"{key}: {data[key]}")
    #print('Contenido: ', response.text) #Contenido en formato texto.
else:
    print('Error: ', response.reason)

####################################
nombre = input(f"Nombre ({data['firstName']}): ")
apellido = input(f"Apellido ({data['lastName']}: ")

if(nombre != ''):
    data['firstName'] = nombre

if(apellido != ''):
    data['lastName'] = apellido

#Llamada para hacer la modificación: put()
url = 'http://school.labs.com.es/api/students/39'
respones = requests.put(url, data=json.dumps(data)) #Convertir a json.

print('Código de Estado: ', response.status_code)
print('Estado: ', response.reason)

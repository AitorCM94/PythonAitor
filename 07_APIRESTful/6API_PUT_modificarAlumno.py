import requests
import json
#CONSULTAR EL ALUMNO POR EL IDENTIFICADOR -> GET
#1. Construcción de la llamada:
url = 'http://school.labs.com.es/api/students/'
idAlumno = input("ID Alumno: ")
headers = {'Content-Type': 'application/json'} #IMPORTANTE AÑADIR EL HEADERS (POST-PUT)
data = None #Variable para los datos del alumno.
#1.1 Llamada en modo get con el input id:
response = requests.get(url + idAlumno)
#1.2 Comprobamos que la llamada se ha realizado correctamente:
print('Código de Estado: ', response.status_code)
print('Estado: ', response.reason)

#2. Pintamos los datos:
if (response.status_code == 200):
    data = response.json() #Convertir la respuesta para obtener el diccionario.
    
    for key in data.keys(): #Para pintar cada una de las propiedades (claves -> .keys()) del diccionario.
        if(key == 'id'): #Para que no pinte de nuevo el ID.
            continue
        print(f"{key}: {data[key]}")

else:
    print('Error: ', response.reason)


#MODIFICAR LOS DATOS -> PUT:
#1. Preguntamos por los nuevos datos:
nombre = input(f"Nombre ({data['firstName']}): ") #Entre paréntesis el valor actual.
apellido = input(f"Apellido ({data['lastName']}): ")
classID = input(f"Clase ({data['classId']}): ")

#2. Incorporamos los nuevos datos a cada una de las claves del diccionario alumno:
if(nombre != ''):
    data['firstName'] = nombre

if(apellido != ''):
    data['lastName'] = apellido

if(classID != ''):
    data['classId'] = int(classID) #Lo convertimos en entero.

#3. Llamada en modo put para hacer la modificación:
response = requests.put(url + idAlumno, headers=headers, data=json.dumps(data)) #Url+id, los nuevos datos en data(BODY)=data(TEXTO) -> Convertidos a json con json.dumps()
#Returns 204 -> No content.

#4. Pintamos si la query se ha realizado correctamente:
if (response.status_code == 204): 
    print("Registro modificado correctamente.")
else:
   print(f"Error: {response.reason}")


#print('Código de Estado: ', response.status_code)
#print('Estado: ', response.reason)

import requests #Es el objeto que representa la conexión http.

#LLAMADA AL MICROSERVICIO:
response = requests.get('http://api.open-notify.org/iss-now.json') #Llamada en modo GET. Retorna un objeto de tipo Response.

#CÓDIGOS DE ESTADO:
print('Código de Estado: ', response.status_code) #Código de estado -> Me va a decir si la comunicación se ha realizado correctamente.
print('Estado: ', response.reason) #Código de estado en formato texto.

#Pintar cabeceras y contenido:
if (response.status_code == 200): #Codigo de estado 200 -> La llamada se ha realizado correctamente!
    #print('Cabeceras: ', response.headers) #Cabeceras -> 'Server', 'Date', 'Content-Type', 'Content-Length', 'Connection'.
    #print('Tipo del contenido: ', response.headers['Content-Type']) #Pintamos el formato con el que trabaja la aplicación -> application/json.

    #print("Contenido: ", response.text) #Pinta el contenido de la respuesta en formato texto (str).
    #print("Contenido original: ", response.content) #Pinta el contenido original (bytes).

    if(response.headers['Content-Type'] == 'application/json'): #Si el contenido trabaja en formato json:
        data = response.json() #Convertimos la respuesta en un objeto JSON (serializado) -> Diccionario.
        #PINTAMOS EL CONTENIDO:
        print('Latitud: ', data['iss_position']['latitude']) #Clave1 del diccionario y clave2 del diccionario dentro clave1.
        print('Longitud: ', data['iss_position']['longitude']) #Clave1 del diccionario y clave2 del diccionario dentro clave1.
        print('Timestamp: ', data['timestamp'])
        print('Mensaje: ', data['message'])
    else:
        print("Formato no compatible.")
        
else:
    print('Error: ', response.reason)
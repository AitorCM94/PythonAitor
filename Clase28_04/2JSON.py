import json

citricos = ["naranja", "limón", "pomelo", "lima"]

#Pasar un objeto a JSON
listaJSON = json.dumps(citricos)
print(listaJSON)

#Pasar de JSON a objeto
lista = json.loads(listaJSON)
print(lista[2]) #Nos permite tratarlo otra vez como a un objeto.
import json

file = open("C:\\Users\\aitor\\OneDrive\\Documentos\\GitHub\\PythonAitor\\fichero.json","rt")
dataJSON = file.read() #Leemos todo el contenido del fichero
file.close()

customers = json.loads(dataJSON) #Transforma el texto en una lista.

print(type(dataJSON))
print(type(customers))

print(len(customers))
print(customers[0]['City']) #Una lista [posicion] donde cada elemento es un Diccionario [clave]


#'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax'
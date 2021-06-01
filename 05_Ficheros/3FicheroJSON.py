import json #Para trabajar con JSON tenemos que importar el módulo json.

#LECTURA DEL FICHERO:
file = open(".\\05_Ficheros\\fichero.json","rt", encoding="UTF-8") #Modo lectura.
dataJSON = file.read() #Leemos todo el contenido del fichero. Variable <class 'str'>.
file.close()

#PASAR DE JSON A OBJETO:
customers = json.loads(dataJSON) #Transformamos el texto JSON a un objeto de tipo <class 'list'>.
#print(len(customers)) #Como es una lista, podemos ver el numero de clientes (elementos de la lista).
#print(customers[0]['City']) #Y con la [posicion] podemos acceder a cada elemento. Los clientes a su vez estan en formato Diccionario [clave] ->:[valor].

#print(customers[0].keys()) #Para pintar las claves del diccionario customers[0]
#CLAVES: 'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax'.
#ID: ANATR, ANTON... Son de tipo texto.

#DEFINICIÓN DE LA FUNCIÓN PARA PINTAR:
def PrintData(customer): #Recibe el resultado de la búsqueda.
    print(f"CustomerID: {customer['CustomerID']}") #Elemento cliente (un diccionario), entre corchetes la clave ('alfanumerica').
    print(f"Company: {customer['CompanyName']}")
    print(f"Contact: {customer['ContactName']} ({customer['ContactTitle']})")
    print(f"Address: {customer['Address']}")
    print(f"         {customer['PostalCode']}, {customer['City']}, {customer['Country']}")
    print(f"Phone: {customer['Phone']}  Fax: {customer['Fax']}")


inID = input("ID: ") #Pedimos el ID

#DEFINICIÓN DE LA FUNCIÓN PARA FILTRAR:
search = list(filter(lambda customer: customer['CustomerID'] == inID, customers)) #Devuelve el customer (lista) que coincida con el input.

if (len(search) == 0):
    print("Not found.")
else:
    PrintData(search[0]) #Del resultado de la búsqueda mando el que está en la posición [0] -> El identificador (único).
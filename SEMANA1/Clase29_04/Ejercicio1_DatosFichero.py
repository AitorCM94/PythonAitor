#CLASE CLIENTE -> Plantilla para crear objetos con la información de los clientes.
class Cliente:
    Identificador   = None
    Nombre          = None
    Apellidos       = None
    Genero          = None
    Pais            = None
    FechaNacimiento = None

    def __init__(self, identificador, nombre, apellidos): #Constructor.
        self.Identificador  = identificador
        self.Nombre         = nombre
        self.Apellidos      = apellidos
########################################################################################################

fichero = open(".\\SEMANA1\\Clase29_04\\fichero.txt", "rt") #Abrimos el fichero -> objeto del tipo <class '_io.TextIOWrapper'>
ClientesVol = [] #Variable lista inicialmente vacía donde volcamos todos los objetos cliente con sus parámetros. ¿Tendriamos 5000 objetos? Sí

#RECORRER Y SEPARAR TODOS LOS DATO DEL FICHERO.
listafichero = fichero.readlines() #Utilizamos la función .readlines() para pasarlo a tipo <class 'list'>. Cada linea es una posicion.
for posicion in listafichero: #Utilizamos el for para recorrer el fichero linea por linea.
    dato = posicion.split(",") #Utilizamos la función .split() para separar los datos de las lineas. Pasa la linea a tipo <class 'list'>
    #VOLCADO DE INFORMACIÓN A UN OBJETO, USANDO LA CLASE:
    #Para no volcar la primera linea (que no contiene información de un cliente): #(también lo podriamos hacer con un contador o un rango).
    if (dato[0].isdigit() == True): #Preguntamos si la primera posición de las lista linea es un numero.
        cliente = Cliente(dato[7], dato[1], dato[2]) #Variable donde instanciamos el objeto con los parámetros -> Datos de la lista del fichero.
        ClientesVol.append(cliente) #Utilizamos la función .append() para añadir los parámetros (datos) del objeto (cliente) a la variable lista (ClientesBus).
print(f"{len(ClientesVol)} clientes importados.")

fichero.close() #Cerramos el fichero. Siempre.


#Una vez Instanciado el objeto con los datos del fichero, podemos acceder a todas las funciones y propiedades definidas dentro de la clase.
"""
#Ejemplo pintando los nombres:
for posicion in ClientesVol:
    print(posicion.Nombre) #Podemos usar los parámetros del objeto, en este caso el Nombre.
"""
"""
#Preguntar por X parámetros (en este caso Nombre, Apellidos y Id) del objeto de la posición X:
while(True): #De esta forma siempre se ejecuta.
    posicion = input("Dime una posición: ") #Preguntamos la posición.
    
    if(posicion.lower() == "fin"): #Para romper el while.
            break
    else:
        print(f"{ClientesVol[int(posicion)].Nombre} {ClientesVol[int(posicion)].Apellidos} {ClientesVol[int(posicion)].Identificador}")
"""

#FILTROS DE BÚSQUEDA:
#Ejemplo:
numeros = [2,45,76,345,87,3,0,234,32,5]
#Definición de una función para buscar números más grandes que 100:
def Func(numero):
    if(numero > 100):
        return True
    else:
        return False
#Uso de la función filter(con la función que hemos definido, en la lista numeros): (epsecificando que se trata de una lista)
#resultado = list(filter(Func, numeros))

#Lo mismo, usando directamente una función lambda:
resultado = list(filter(lambda numero: numero > 100, numeros)) #Hace exactamente lo mismo que con la Func definida.
print(resultado)

"""
#Definición de la función que me permite buscar con el identificador:
def FiltroID(cliente): #Por parametro siempre vamos a recibir los elementos de una colección. En este caso los de la lista ClientesVol, que son los objetos cliente.
    if(cliente.Identificador == "2468"): #Si el identificador del objeto cliente coincide con el que queremos, devuelve True.
        return True
    else:
        return False
#Uso de la función creada con la función de python filter():
resultado = filter(FiltroID, ClientesVol) #Retorna el objeto que coincide.
print(resultado)
"""
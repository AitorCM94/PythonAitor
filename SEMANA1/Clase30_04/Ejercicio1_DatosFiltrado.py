#CLASE CLIENTE -> Plantilla para crear objetos con la información de los clientes.
class Cliente:
    Nombre          = None
    Apellidos       = None
    Genero          = None
    Pais            = None
    Edad            = None
    FechaAlta       = None
    Identificador   = None

    def __init__(self, identificador, nombre, apellidos): #Constructor.
        self.Identificador  = identificador
        self.Nombre         = nombre
        self.Apellidos      = apellidos
########################################################################################################
from datetime import datetime

fichero = open(".\\SEMANA1\\Clase29_04\\fichero.txt", "rt")
ClientesVol = []

#RECORRER Y SEPARAR TODOS LOS DATO DEL FICHERO.
listafichero = fichero.readlines()
for posicion in listafichero:
    dato = posicion.split(",")
    if (dato[0].isdigit() == True):
        cliente = Cliente(dato[7].strip(), dato[1].strip(), dato[2].strip()) #Instancia el objeto. Volcamos los datos al constructor. (eliminamos los espacios)
        cliente.Genero = dato[3].strip() #Añadimos el dato del genero a la propiedad .Genero del objeto cliente.
        cliente.Edad = int(dato[5].strip()) #Añadimos la edad transformandola en un número int() para poder hacer operaciones.
        cliente.Pais = dato[4].strip() #Añadimos el Pais a las propiedades del objeto.
        cliente.FechaAlta = datetime.strptime(dato[6].strip(), "%d/%m/%Y").date() #Añadir la fecha convirtiendola con el mismo formato que en el fichero.
        ClientesVol.append(cliente) #Volcamos la información a la lista ClientesVol.
print(f"{len(ClientesVol)} clientes importados.")

fichero.close()


#FILTRADOS:
#Definición de las funciones que me permite buscar contenidos:
def FiltroID(cliente): #Por parametro siempre vamos a recibir los elementos de una colección. En este caso los objetos cliente de la lista ClientesVol.
    if(cliente.Identificador == "2468"): #Si el identificador del objeto cliente coincide con el que queremos, devuelve True.
        return True
    else:
        return False
def GeneroM(cliente):
    if(cliente.Genero == "Male"): #Podriamos usar una variable externa para rellenar ese valor "Male/Female" para tener solo una función.
        return True
    else:
        return False
def GeneroF(cliente):
    if(cliente.Genero == "Female"):
        return True
    else:
        return False

#Uso de la función creada con la función de python filter():
resultadoID = list(filter(FiltroID, ClientesVol)) #Filter: Retorna el objeto que coincide. List: especificar que es una lista.
resultadoM = list(filter(GeneroM, ClientesVol))
resultadoF = list(filter(GeneroF, ClientesVol))

#Uso con funciones lambda:
resultadoID = list(filter(lambda cliente: cliente.Identificador == "2468", ClientesVol))
resultadoM = list(filter(lambda cliente: cliente.Genero == "Male", ClientesVol))
resultadoF = list(filter(lambda cliente: cliente.Genero == "Female", ClientesVol))

#CONCATENAR COMPARACIONES (AND/OR):
#Clientes menores de 26 años de Francia:
print(f"{len(list(filter(lambda cliente: cliente.Edad < 26 and cliente.Pais == 'France', ClientesVol)))} clientes menores de 26 años de Francia.")
#Clientes hombres de Estados Unidos:
print(f"{len(list(filter(lambda cliente: cliente.Genero == 'Male' and cliente.Pais == 'United States', ClientesVol)))} clientes hombres de Estados Unidos.")
#Clientes mujeres de 26 años de Inglaterra:
print(f"{len(list(filter(lambda cliente: cliente.Genero == 'Female' and cliente.Edad == 26 and cliente.Pais == 'Great Britain', ClientesVol)))} clientes mujeres de 26 años de Inglaterra.")

#BUSCANDO DE MANERA DINÁMICA, PREGUNTANDO INPUTS:
inEdad = int(input("Edad: "))
inPais = input("Pais (France/Great Britain/United States): ")
inGenero = input("Genero (Female/Male): ")

print(f"{len(list(filter(lambda cliente: cliente.Edad == inEdad and cliente.Pais == inPais and cliente.Genero == inGenero, ClientesVol)))} clientes.")
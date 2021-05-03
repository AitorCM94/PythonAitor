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

fichero = open(".\\SEMANA1\\Clase29_04\\fichero.txt", "rt") #Abrimos el fichero de texto en modo lectura.
ClientesVol = []

#RECORRER Y SEPARAR TODOS LOS DATO DEL FICHERO.
listafichero = fichero.readlines()
for posicion in listafichero:
    dato = posicion.split(",")
    if (dato[0].isdigit() == True):
        cliente = Cliente(dato[7].strip(), dato[1].strip(), dato[2].strip())
        cliente.Genero = dato[3].strip()
        cliente.Edad = int(dato[5].strip())
        cliente.Pais = dato[4].strip()
        cliente.FechaAlta = datetime.strptime(dato[6].strip(), "%d/%m/%Y").date()
        ClientesVol.append(cliente)
print(f"{len(ClientesVol)} clientes importados.")

fichero.close()


#FILTRADOS:
inEdad = int(input("Edad: "))
inPais = input("Pais (France/Great Britain/United States): ")
inGenero = input("Genero (Female/Male): ")

resultado = list(filter(lambda cliente: cliente.Edad == inEdad and cliente.Pais == inPais and cliente.Genero == inGenero, ClientesVol)) #Nos devuelve una lista.
print(f"{len(resultado)} clientes.")
"""
#MÉTODOS DE AGREGAR TEXTO A UN FICHERO:
#Método1: Escribir añadiendo línea por línea (write): 
fichero2.write("Hola Aitor.\n") #Especificando el salto de línea (\n)
fichero2.write("Hola Aitor.\n")
#Método2: Escribir añadiendo una colección (writelines):
lineas = [] #Creamos la lista.
lineas.append("Linea1: Hola Aitor\n") #Añadimos los elementos a la lista.
lineas.append("Linea2: Hola Aitor\n")
fichero2.writelines(lineas) #Usamos la función.
"""
#PASAR LA INFORMACIÓN A OTRO FICHERO:
fichero2 = open("Resultados.txt", "wt") #Abrimos un nuevo fichero de texto en modo escritura.

fichero2.write("Row,First Name,Last Name,Gender,Country,Age,Date\n") #Agregamos la primera línea (que es diferente al resto).
contador = 0
for cliente in resultado: #Con el for recorremos cada cliente objeto (del resultado que nos ha dado el filtrado) y pintamos por orden sus atributos.
    contador += 1 #Para añadir la posición del objeto cliente en Row.
    fichero2.write(f"{contador},{cliente.Nombre},{cliente.Apellidos},{cliente.Genero},{cliente.Pais},{cliente.Edad},{cliente.FechaAlta.strftime('%d/%m/%Y')}\n")

fichero2.close()
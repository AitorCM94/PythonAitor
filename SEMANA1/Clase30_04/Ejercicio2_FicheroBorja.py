from datetime import datetime
"""
def BuscarClienteID(item):
    if(item.Identificador == "1562"):
        return True
    else:
        return False

def BuscarHombre(item): #Entra la clase cliente
    if(item.Genero == "Male"):
        return True
    else:
        return False

def BuscarMujeres(item):
    if(item.Genero == "Female"):
        return True
    else:
        return False

def BuscarPais(item):
    if(item.Pais == "United States"):
        return True
    else:
        return False

def BuscarEdad(item):
    if(item.Edad == EdadIn):
        return True
    else:
        return False

def BuscarEdadPais(item):
    if(item.Edad >= 26 and item.Pais == "France"):
        return True
    else:
        return False

def BuscarPaisEdad(item):
    if (item.Pais == "Great Britain" and item.Edad <= 26):
        return True
    else:
        return False
"""

#########################################################
class Cliente:
    Identificador   = None
    Nombre          = None
    Apellidos       = None
    Genero          = None
    Pais            = None
    Edad            = None
    FechaAlta       = None

    def __init__(self, id, nombre, apellidos) -> None:
        self.Identificador = id
        self.Nombre = nombre
        self.Apellidos = apellidos
        
###########################################################
path = "C:\\Users\\aitor\\OneDrive\\Documentos\\GitHub\\PythonAitor\\Clase29_04\\fichero.txt"
clientes = []


file = open(path)
for linea in (file.readlines()):
    data = linea.split(",")
    if(data[0].isdigit() == True):    
        #clientes.append(Cliente(data[7], data[1], data[2]))  
        cliente = Cliente(data[7].strip(), data[1].strip(), data[2].strip())
        cliente.Edad = int(data[5].strip()) #Pasar la edad a números para realizar calculos.
        Cliente.Pais = data[4].strip()
        clientes.append(cliente)

        cliente.FechaAlta = datetime.strptime(data[6].strip(), "%d/%m/%Y").date()
file.close()

e = int(input("Edad: "))
p = input("Pais (France, United States, Great Britain): ")
g = input("Genero (Female o Male): ")
#print(f"{len(list(filter(lambda x: x.Edad == e and x.Pais == p and x.Genero == g, clientes)))}")

resultado = list(filter(lambda x: x.Edad == e and x.Pais == p and x.Genero == g, clientes))

file2 = open("resultado.txt", "wt")
file2.write("Row,First Name,Last Name,Gender,Country,Age,Date")
contador = 0
for item in resultado:
    file2.write(item)
    contador+=1

file2.close()

#print(len(list(filter(BuscarEdad, clientes))))

#Pais = input("Pais: ")

#Genero = input ("Genero: ")

#print(f"{len(clientes)} clientes importados.")
#print(clientes[0].Identificador)

#print(clientes[3].Genero)

#print(len(list(filter(BuscarHombre, clientes))))
#print(len(list(filter(BuscarMujeres, clientes))))
#lambda item: item.Genero == "Male", clientes

#print(len(list(filter(BuscarPais, clientes))))
#print(len(list(filter(BuscarEdadPais, clientes))))
#print(len(list(filter(BuscarPaisEdad, clientes))))

#resultado = list(filter(BuscarClienteID, clientes))
#print(len(resultado))
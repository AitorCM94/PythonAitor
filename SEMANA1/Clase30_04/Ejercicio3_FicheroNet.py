from datetime import datetime
##########################################################
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
clientesList = []


file = open(path)
for linea in (file.readlines()):
    data = linea.split(",")
    if(data[0].isdigit() == True):    
        #clientes.append(Cliente(data[7], data[1], data[2]))  
        cliente = Cliente(data[7].strip(), data[1].strip(), data[2].strip())
        cliente.Edad = int(data[5].strip()) #Pasar la edad a números para realizar calculos.
        cliente.Pais = data[4].strip()
        clientesList.append(clientesList)

        cliente.FechaAlta = datetime.strptime(data[6].strip(), "%d/%m/%Y").date()
file.close()

e = int(input("Edad: "))
p = input("Pais (France, United States, Great Britain): ")
g = input("Genero (Female o Male): ")
#print(f"{len(list(filter(lambda x: x.Edad == e and x.Pais == p and x.Genero == g, clientesList)))} clientes coincidentes.")

resultado = list(filter(lambda x: x.Edad == e and x.Pais == p and x.Genero == g, clientesList))

file2 = open("resultado.txt", "wt")
file2.write("Row,First Name,Last Name,Gender,Country,Age,Date")
for item in resultado:
    file2.write(item)


file2.close()
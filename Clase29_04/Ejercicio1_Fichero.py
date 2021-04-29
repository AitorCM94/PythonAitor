class Cliente:
    Identificador   = None
    Nombre          = None
    Apellidos       = None
    Genero          = None
    Pais            = None
    FechaNacimiento = None

    def __init__(self, identificador, nombre, apellidos): #Creación del constructor.
        self.Identificador  = identificador
        self.Nombre         = nombre
        self.Apellidos      = apellidos


fichero = "C:\\Users\\aitor\\OneDrive\\Documentos\\GitHub\\PythonAitor\\Clase29_04\\fichero.txt"
clientes = [] #Llenar con los datos de fichero.

for linea in (open(fichero).readlines()):
    fichero = linea.split(",") #con el split transformamos el texto en una lista.
    
    if (linea[0].isdigit() == True): #Preguntar si linea posición 0 es un digito.
        #clientes.append(Cliente(fichero[1], fichero[2], fichero[7]))
        cliente = Cliente(fichero[1], fichero[2], fichero[7]) #Creamos una variable cliente temporal.
        clientes.append(cliente) #añadir la información en la variable
    
    #print(linea)
    #print(linea[2])
    #print(fichero)
    #print(fichero[2])
    #for n in fichero: #pinta cada uno de los elementos de la colección.
    #    print(n)
    #break #Para hacerlo solo con la primera línea.
    
#for c in clientes:
#    print(c.Nombre)

#Definición de la función que te permite buscar por el identificador de cada cliente.






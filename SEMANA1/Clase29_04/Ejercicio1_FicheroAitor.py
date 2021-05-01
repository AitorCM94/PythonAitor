#Clase Cliente: Plantilla para crear objetos con la información de los clientes.
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



fichero = open(".\\SEMANA1\\Clase29_04\\fichero.txt", "rt") #Abrimos el fichero -> Nos devuelve un objeto del tipo <class '_io.TextIOWrapper'>
#contenido = fichero.read() #Utilizamos la función .read() para que nos devuelva el contenido del fichero como una variable de tipo <class 'str'>.
linea = fichero.readlines() #Utilizamos la función .readlines() para que nos devuelva el contenido del fichero en formato de <class 'list'> -> Cada línea es un elemento.




#C:\\Users\\aitor\\OneDrive\\Documentos\\GitHub\PythonAitor
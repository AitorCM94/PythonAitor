#Añadir dos funciones: Una que me sirva para añadir la fecha de nacimiento -> En input. Otra función para calcular la edad y la pinte.
from datetime import datetime

class ObjetoAlumno: #Creación del objeto Alumno.
    Nombre          = None
    Apellido1       = None
    Apellido2       = None
    FechaNacimiento = None
    #CONSTRUCTOR: Tiene como finalidad inicializar las variables. Añadiendo argumentos obligamos a que se introduzcan esos parámetros cuando instanciamos el objeto.
    def __init__(self, Nombre, Apellido1, Apellido2) -> None: #Guardamos los parámetros pedidos en las variables del objeto clase.
        self.Nombre    = Nombre 
        self.Apellido1 = Apellido1 #Self. siempre hace referencia a las variables de la clase.
        self.Apellido2 = Apellido2 
            
    def getNombreCompleto (self) -> str: #No hace falta poner argumentos por que ya los coge de la clase, que los obtiene con la función constructor.
        return print(f"{self.Nombre} {self.Apellido1} {self.Apellido2}")

    def getFechaNacimiento(self, fecha) -> None: #Añadiendo el argumento fecha pedimos que para usar la función devemos especificar un parámetro (fecha).
        self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()

    def edad(self) -> int:
        edad = datetime.now().date().year - self.FechaNacimiento.year
        return edad

#############PARTE PRINCIPAL DEL PROGRAMA################### -> Es donde según la información retornada por las funciones pintamos los resultados.

#Instanciamos el Objeto, se ejecuta la función constructor.
VarAlumno = ObjetoAlumno("Aitor", "Cerdán", "Mañé")
print(type(VarAlumno))

#Invocamos a las funciones del objeto
VarAlumno.getNombreCompleto()
VarAlumno.getFechaNacimiento(input("Escribe tu fecha de nacimiento (dd-mm-AAAA): "))
print(VarAlumno.edad())


#------------------Pasar parámetros de manera desordenada------------------#
"""
#Parámetros constructor:
def __init__(self, Nombre, Apellido1="", Apellido2) -> None: #Apellido1 podría quedar vacío.
        self.Nombre    = Nombre 
        self.Apellido1 = Apellido1
        self.Apellido2 = Apellido2

#Parámetros al instanciar el objeto:
variable = objeto(Apellido2=Mañé, Nombre=Aitor)
"""
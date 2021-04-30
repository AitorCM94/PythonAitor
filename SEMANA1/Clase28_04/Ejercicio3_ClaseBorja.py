from datetime import datetime

#Creamos una clase utilizando class -> LAS CLASES FUNCIONAN COMO UNA PLANTILLA PARA LA CREACIÓN DE OBJETO, NUNCA CONTIENEN INFORMACIÓN.
class Alumno:
    #Variables o Propiedades de la clase
    Nombre          = None
    Apellido1       = None
    Apellido2       = None
    FechaNacimiento = None

    #Función constructor se ejecuta al crear el objeto
    #self representa al mismo objeto clase
    def __init__(self, nombre, apell1, apell2) -> None:
        self.Nombre    = nombre
        self.Apellido1 = apell1
        self.Apellido2 = apell2

    def getNombreCompleto(self) -> None:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

    def setFechaNacimiento(self, fecha) -> bool: #Retornamos un Bolean en funcion de si la fecha ha sido introducida correctamente o no.
        try:
            if(len(fecha) == 8):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            return True
        except:
            return False
            pass

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None): 
            return -1 #Si no tenemos fecha de nacimiento la función retorna "-1", lo que generalmente se utiliza para indicar un error.
        else:
            return datetime.now().year - self.FechaNacimiento.year

#############PARTE PRINCIPAL DEL PROGRAMA################### -> Es donde según la información retornada por las funciones pintamos los resultados.

#Instanciamos el Objeto, se ejecuta la función constructor
Nom = input("Nombre: ")
Ap1 = input("Primer apellido: ")
Ap2 = input("Segundo apellido: ")

alumno = Alumno(Nom, Ap1, Ap2) #Volcamos las variables que contienen inputs como parametros del objeto.

FechaNacimiento = input("Pon tu fecha de nacimiento: ")

#Invocamos a las funciones del objeto
alumno.setFechaNacimiento(FechaNacimiento)
print(f"Edad: {alumno.getEdad()}")

#Capturamos el True/False de si la fecha ha sido introducida correctamente para mostrarlo en pantalla:
if (alumno.setFechaNacimiento(FechaNacimiento) == True): #Invocación de la función del objeto Alumno. También la podríamos almacenar en una variable.
    print("Fecha introducida correctamente.")
else:
    print("No es correcto.")

############################################################

#USO DE LA FUNCIÓN SPLIT PARA MANEJAR INFORMACIÓN EN TEXTO:
n = "Aitor Cerdán Mañé" #Información en texto.
datos = n.split(" ") #Conversión a ARRAY.
for d in datos: #Pintar cada elemento por separado.
    print(d)

#Crar un objeto alumno con los datos introducidos:
alumno0 = Alumno(datos[0], datos[1], datos[2])
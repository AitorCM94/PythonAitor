#Pregunta la fecha de nacimiento
from datetime import datetime

fechaNacimiento = input("Fecha de nacimiento: ")
fechaNacimiento = datetime.strptime(fechaNacimiento, "%d-%m-%Y").date()

#print(fechaNacimiento)

#Calcula la edad
fechaActual = datetime.now().date()
#print("Fecha1: ", fechaActual.strftime("Dia: %j del año %Y"))

edad = fechaActual.year - fechaNacimiento.year

#print(edad)

#Mostrar por pantalla: Tienes XX años, eres mayor de edad

if (edad >= 18):
    print(f"Tenes {edad} años, eres mayor de edad")

#Te faltan xx alos para ser mayor de edad.
#elif(edad < 18):
 #   print(f"Te faltan {18 - edad}")
else:
    print(f"Te faltan{(18-edad)} años para ser mayor de edad.")
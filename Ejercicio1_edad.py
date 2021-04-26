from datetime import datetime
#Pedir y convertir la fecha
fechaNacimiento = input("Fecha de nacimiento: ")
fechaNacimiento = datetime.strptime(fechaNacimiento, "%d-%m-%Y").date()

#Calcular la edad
fechaActual = datetime.now().date()
edad = fechaActual.year - fechaNacimiento.year

#Mostrar la edad
if (edad >= 18):
    print(f"Tenes {edad} años, eres mayor de edad")
#elif(edad < 18):
#   print(f"Te faltan {(18 - edad)} años para ser mayor de edad.")
else:
    print(f"Te faltan{(18-edad)} años para ser mayor de edad.")
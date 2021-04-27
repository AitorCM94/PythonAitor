"""
Pregunta la fecha de nacimiento del operador
Calcula la edad
Muestra por pantalla el mensaje correspondiente:
a. Tienes xx años, eres mayor de edad.
b. Te faltan xx años para ser mayor de edad.
"""

from datetime import datetime
#Pedir y convertir la fecha
fechaNacimiento = input("Fecha de nacimiento: ")
fechaNacimiento = datetime.strptime(fechaNacimiento, "%d-%m-%Y").date()

#Calcular la edad
fechaActual = datetime.now().date() #FECHA QUE TIENE EL SISTEMA
edad = fechaActual.year - fechaNacimiento.year

#Mostrar la edad
if (edad >= 18):
    print(f"Tenes {edad} años, eres mayor de edad")

else:
    print(f"Te faltan{(18-edad)} años para ser mayor de edad.")


#EJERCICIO EN REPOSITORIO DE BORJA: 01_Calcular-la-Edad.py -> Lo reduce en una sola línea/sentencia.
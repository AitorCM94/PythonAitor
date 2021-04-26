from datetime import datetime

dt1 = datetime.now().date()
print("Fecha1: ", dt1.strftime("Dia: %j del año %Y"))

dt2 = datetime.now()
#print("Fecha2: ", dt2)

#print("Fecha de nacimiento: ")
fecha = input("Fecha de nacimiento: ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()
años = dt1.year - dt3.year

#print("Fecha3: ", dt3)
print(f"Tienes {años} años.")
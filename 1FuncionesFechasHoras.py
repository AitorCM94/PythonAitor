from datetime import datetime #IMPORTACIÓN DE UNA LIBERIA -> import datetime. Y dentro de esa libreria el objeto definido -> datetime

datenow1 = datetime.now() #.now() nos devuelve el momento de ahora en: Fecha y hora.
print("Fecha de .now(): ", datenow1)

datenow2 = datetime.now().date() #.now() con .date() nos devuelve solo la Fecha / .today() nos daría la fecha de hoy.
print("Fecha de .now().date(): ", datenow2)
print("Fecha formateada: ", datenow2.strftime("%A, %dth of %b %Y")) #Usamos la función strformat() para formatearla usando comodines %.


print()
#Mostrar información desgranada: .year, .month, .day, .hour, .minute, .second...
print("Año: ", datenow2.year)
print("Mes: ", datenow2.month)
#Con las variables formateadas
print("Día: {n:6.0f}".format(n=datenow2.day))
print(f"Hora: {datenow1.hour}:{datenow1.minute}")
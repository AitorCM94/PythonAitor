from datetime import datetime #Importación de la libreria datatime -> objeto datatime
from pytz import timezone #Importación de la libreria pytz -> objeto timezone

import pytz #Objeto nativo de python -> Para pintar todas las zonas.
print(pytz.all_timezones) #Pinta todas las zonas horarias.

#Pintar una zona horaria: fecha / hora / diferencia horaria (siempre en referencia a la hora universal)
print(datetime.now(pytz.timezone('Europe/Madrid'))) #Función .now -> el momento de ahora / Función .timezone() -> zona horaria de los paises
print(datetime.now(pytz.timezone('US/Alaska'))) # =
print(datetime.now(pytz.timezone('UTC'))) # Hora universal (del meridiano de greenwich)
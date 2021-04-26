import time #Objeto nativo de python (no está en una libreria aparte)

#Estructura de la función: [objeto].[función]()

print("Tiempo: ", time.time()) # Retorna el tiempo actual. Muestra el "sello" (stamp) de tiempo, valores numéricos.
print(time.localtime()) # Retorna una representación local de todos los (argumentos) de tiempo. Lo muestra con una estructura.

#Mostrar información desgranada: .year, .month, .day, .hour, .minute, .second...
print("Año: ", time.localtime().tm_year) #.tm_year -> Año
print("Minutos: ", time.localtime().tm_min) #.tm_min -> Minutos
print("Milisegundos: ", int(time.time() * 1000.0)) #int() -> Para pasar de texto a número el(tiempo actual X 1000.0) ¿?

print(time.asctime()) #Función que retorna una representación del tiempo alfanumérica: fecha, hora y día de la semana.
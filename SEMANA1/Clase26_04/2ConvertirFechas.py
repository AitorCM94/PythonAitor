from datetime import datetime

#Convertir la variable objeto de alfanumérico a FECHA -> Esto nos dara funciones y propiedades distintas: fecha.[funciones/propiedades]
fechaTexto = "14-10-1994" #Fecha en texto.
fechaFecha = datetime.strptime(fechaTexto, "%d-%m-%Y").date() #Usamos la función strptime() y especificamos el patron del texto %d-%m-%Y (Y en mayúscula son 4 dígitos).
print("Fecha: ", fechaFecha)

#Utilizando el input()
fechaTexto = input("Escribe una fecha: ") #El resultado del input siempre sera un alfanumérico.
fechaFecha = datetime.strptime(fechaTexto, "%d-%m-%Y").date() 
print(f"Fecha: {fechaFecha.day}-{fechaFecha.month}-{fechaFecha.year}") #Formateamos la variable para que aparezcan dd-mm-yyyy.

#Operaciones con las fechas
fechaNacimientoTexto = input("Fecha de nacimiento: ") #Recogemos la variable fecha.
fechaNacimiento = datetime.strptime(fechaNacimientoTexto, "%d-%m-%Y").date() #La pasamos a formato fecha.
fechaActual = datetime.now().date() # Variable con la fecha actual.

años = fechaActual.year - fechaNacimiento.year #Operación para calcular los años. DEFINIMOS EL DATO QUE QUEREMOS -> .year

print(f"Tienes: {años} años.")
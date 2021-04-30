from datetime import datetime

#Creación de la función1 (pide parámetros pero no retorna datos):
def saluda(nombre): #Entre paréntesis definición de los argumentos.
    print(f"Hola {nombre}!!!") #Uso de los arguementos.

#Creación de la función2 (pide parámetros y retorna un dato):
def contador(frase):
    caracteres = 0
    caracteres = len(frase)
    return caracteres

#Creación de la función3 (no pide parámetros pero retorna datos):
def diaA():
    return datetime.now().date().strftime("%A")


#Uso de la función1:
saluda("Aitor") #Introducción de los parámetros -> argumentos.

#Uso de la función2:
print(contador("En un lugar de la mancha..."))

#Uso de la función3:
print(diaA())

"""
Pregunta los metros recorridos (dividir entre 1000 para pasar a km)
Pregunta el tiempo en minutos empleado (Dividir entre 60 para pasar a horas)
Calcula la velocidad km/h. (Formula: distancia/tiempo)
Muestra por pantalla el mensaje correspondiente:
a. Inferior a 30km/h -> Velocidad Baja
b. Mayor de 30km/h e inferior de 75km/h -> Velocidad Moderada
c. Mayor de 75km/h -> Velocidad Alta
"""
#SOLUCIÓN BORJA
disMe = input("Metros recorridos: ")
timMi = input("Minutos empleados: ")

disKm = float(disMe) / 1000 #Pasa el texto a número decimal. Pasa de metros a Km.
timHo = float(timMi) / 60 #Pasa el texto a número decimal. Pasa de minutos a horas.
velocidad = disKm / timHo #Calcula la velocidad media.

#REPOSITORIO BORJA -> Todo lo anterior en una línea/sentencia.

if(velocidad > 75):
    print(f"La velocidad de {velocidad:1.2f} km/h es Alta.")
elif(velocidad < 30):
    print(f"La velocidad de {velocidad:1.2f} km/h es Baja.")
else:
    print(f"La velocidad de {velocidad:1.2f} km/h es Moderada.")

#SOLUCIÓN LYDIA
"""
print("Metros recorridos: ")
metrosR=int(input()) #Para pasar de texto a número.
print("Minutos empleados: ")
minR=int(input()) #Para pasar de texto a número.

velocidad=(metrosR/1000)/(minR/60) #Primero pasa metros a km y minutos a hora. Segundo calcula la velocidad media.
print(velocidad)
if(velocidad<30):
    print("Velocidad baja.")
elif(velocidad>75):
    print("Velocidad moderada")
elif(velocidad>75):
    print("Velocidad alta")
"""

#SOLUCIÓN PROPIA
"""
distancia = input("Metros: ")
tiempo = input("Minutos: ")

distancia = int(distancia)
tiempo = int(tiempo)

velocidad = distancia / tiempo


if (velocidad > 75):
    print("Velocidad Alta")

elif (velocidad > 30):
    print("Velocidad Moderada")

else:
    print("Velocidad Baja")
"""
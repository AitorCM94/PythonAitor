distancia = input("Kilometros: ")
tiempo = input("Tiempo: ")

distancia = int(distancia)
tiempo = int(tiempo)

velocidad = distancia / tiempo


if (velocidad > 75):
    print("Velocidad Alta")

elif (velocidad > 30):
    print("Velocidad Media")

elif (velocidad < 30):
    print("Velocidad Moderada")

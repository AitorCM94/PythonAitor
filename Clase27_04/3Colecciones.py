frutas = ["Naranja", "Limón", "Pomelo", "Líma"]

print(frutas)
print(frutas[2]) #Pintar que elemento está en x posición.

frutas[2] = "Fresa" # Modificar un elemento de una lista
print(frutas)

#Métodos para las colecciones.
frutas.append("Manzana")
print(frutas)
frutas.remove("Limón")
print(frutas)

#Comprovar si un elemento existe en la lista:
elemBus = "Manzana"
if(elemBus in frutas):
    print(f"{elemBus} sí está!")
elif(elemBus not in frutas):
    print(f"{elemBus} no está :(")

#Conocer la posición de un elemento
elemInd = "Manzana"
for elementos in range(0,len(frutas)):
    if(frutas[elementos] == elemInd):
        print(f"Posición {elementos} de la lista.")
if (elemInd not in frutas):
        print(f"{elemInd} no encontrado.")
frutas = ["Naranja", "Limón", "Pomelo", "Líma"]
print(frutas)

#Pintar los elementos de una lista:
for elementos in frutas:
    print(elementos)

#Pintar que elemento está en x posición.
print(frutas[2])

#Modificar un elemento de una lista
frutas[2] = "Fresa" 
print(frutas)

#Comprovar si un elemento existe en la lista:
elemBus = "Manzana"
if(elemBus in frutas):
    print(f"{elemBus} sí está!")
elif(elemBus not in frutas):
    print(f"{elemBus} no está :(")

#Conocer la posición de un elemento:
elemInd = "Manzana"
for elementos in range(0,len(frutas)):
    if(frutas[elementos] == elemInd):
        print(f"Posición {elementos} de la lista.")
if (elemInd not in frutas):
        print(f"{elemInd} no encontrado.")

#Ejemplo de uso de métodos para las colecciones:
frutas.append("Manzana")
print(frutas)
frutas.remove("Limón")
print(frutas)
frutas.sort()
print(frutas)
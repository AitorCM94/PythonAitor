#EJEMPLO BASE DE WHILE
valor = 0
while(valor < 5):
    valor += 1
    if (valor == 3):
        continue
    print(valor)

print("FIN WHILE")


#RECORRER CARÁCTERES
texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme..."
for letra in texto:
    print (letra)

for index in range(len(texto)):
    print(texto[index])


#RECORRER LISTAS
pares = ["casa", "coche", "moto", "perro", "luz", "cama", "sol", "guitarra", "pastel"]
#Posicion: 0       1       2        3       4       5      6         7          8
#Numero de elementos: 9. -> len()

#Con el for:
for posicion in pares: #Recorremos la lista y nos pinta el valor de cada uno de sus elementos.
    print(posicion) #Si pones pares pinta toda la lista tantas veces como elementos tiene.

for posicion in range(len(pares)): #El rango nos va a dar un valor numérico -> el índice (que se corresponde a la posición).
    print(pares[posicion]) #De esta manera indicamos que pinte el valor de cada posicion de la lista.

#Con el while:
posicion = 0
while (posicion < len(pares)):
    print(pares[posicion])
    posicion += 1

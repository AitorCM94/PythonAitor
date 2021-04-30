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
for elementos in pares: #Recorremos la array y nos pinta el valor de cada uno de sus elementos.
    print(elementos) #Si poso pares es pinta la variable pares completa per cada element que la conforma.

for index in range(len(pares)): #El rango nos va a dar un valor numérico (posición de los elementos -> index), no el valor de cada elemento.
    print(pares[index]) # Para que pinte el valor de cada uno de los elementos de la array.
#Con el while:
index = 0
while (index < len(pares)):
    print(pares[index])
    index += 1

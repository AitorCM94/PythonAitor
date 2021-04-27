numero = 0
array = []

contador = 0
while (contador < 10):
    numero = int(input("Escribe numeros: "))
    if (type(numero) is int):
        array.append(numero)
        contador += 1
    else:
        print("No es correcto.")
print(array)

suma = 0
for s in array:
    suma += s
print(suma)

media = suma / len(array)
print (media)

#Pintar cuantos pares hay POR HACER
pares = 0
for p in array:
    pares = p / 2
    if (pares is int):
        prinet(pares.count())



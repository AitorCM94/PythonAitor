


def pedirNum ():
    numero = 0
    array = []
    while (len(array) < 10):
        numero = int(input("Escribe un número: "))
        if (type(numero) is int):
            array.append(numero)
        else:
            print("No es correcto.")
    print(f"Núeros introducidos: {array}.")
    return

print(pedirNum)
"""
suma = 0 
for elemento in array:
    suma += elemento 
print(f"Suma total: {suma}.")

media = suma / len(array)
print (f"La media es: {media}.")

pares = 0
for elemento in array:
    if (elemento%2 == 0):
        pares += 1
print(f"{pares} números pares.")


def impares(array)
impares = 0
for elemento in array:
    if (elemento%2 != 0):
        impares += 1
return

#print(f"{impares} números impares.")
"""
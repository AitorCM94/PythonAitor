numero = 0
array = []

contador = 0
while (contador < 10):
    numero = int(input("Escribe un número: "))
    if (type(numero) is int):
        array.append(numero)
        contador += 1
    else:
        print("No es correcto.")
print(f"Núeros introducidos: {array}.")

suma = 0
for s in array:
    suma += s #se van acumulando uno encima de otro
print(f"Suma total: {suma}.")

media = suma / len(array)
print (f"La media es: {media}.")

pares = 0
for p in array:
    if (p%2 == 0):
        pares += 1
print(f"{pares} números pares.")


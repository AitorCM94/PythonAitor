numero = 0
array = []

contador = 0
while (contador < 10): #Podriamso usar la funcion len() para indicar que dure hasta que pase por todos los elementos de la array.
    numero = int(input("Escribe un número: "))
    if (type(numero) is int):
        array.append(numero)
        contador += 1
    else:
        print("No es correcto.")
print(f"Núeros introducidos: {array}.")

suma = 0 #podemos juntar todas las operaciones con un for -> if -> else // Y después meter todo en el WHILE.
for elemento in array:
    suma += elemento #se van acumulando uno encima de otro
print(f"Suma total: {suma}.")

media = suma / len(array)
print (f"La media es: {media}.")

pares = 0
for elemento in array:
    if (elemento%2 == 0):
        pares += 1
print(f"{pares} números pares.")

impares = 0
for elemento in array:
    if (elemento%2 != 0):
        impares += 1
print(f"{impares} números impares.")

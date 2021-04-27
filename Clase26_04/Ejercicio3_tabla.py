#TABLA DE MULTIPLICAR
numInt = int(input("La tabla del: "))

#Con la función range:
for numero in range (11):
    print(f"{numInt} x {numero:2.0f} = {numInt*numero:2.0f}")

print()

#Con una array:
tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in tabla:
    print(f"{numInt} x {numero:2.0f} = {numInt * numero:2.0f}")

print()

#Preguntando si el valor introducido es un número:
numFor = input("La tabla del: ")

if(numFor.isdigit() == True):
    for numero in range (11):
        print(f"{numFor} x {numero:2.0f} = {int(numFor)*numero:2.0f}") # En el momento de hacer la operación pasa el numero de alfanumerico a número.
else:
    print(f"{numFor}, no es un número.")
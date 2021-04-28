def addItem():
    numeros = []
    while(len(numeros) < 11):
        num = input("Dime un número: ")
        if(num.isdigit()):
            numeros.append(int(num))

addItem()

def operaciones():
    suma = 0
    pares = 0
    impares = 0
    for numero in numeros:
        print(f"Número: {numero}")
        suma += numero
        if(numero % 2 == 0):
            pares += 1
        else:
            impares += 1
#Meter el código a ejecutar en las definiciones de función
#Identificar las variables fijas (las que pedimos) y desacoplarlas creando parámetros.

def addNum(listaVacia):
    while(len(listaVacia) < 10):
            num = input("Dime un número: ")
            if(num.isdigit()):
                listaVacia.append(int(num))
            else:
                print(f"{num} no es correcto.")
                num = ""

def numOper(listaLlena):
    suma = 0
    pares = 0
    impares = 0
    for numero in listaLlena:
        print(f"Número: {numero}")
        suma += numero
        if(numero % 2 == 0):
            pares += 1
        else:
            impares += 1
    print(f"Suma Total: {suma}")
    print(f"Media: {suma / len(numeros)}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    return

numeros = []
addNum(numeros)
numOper(numeros)


#Función normal:
def saluda(nombre):
    print(f"Hola {nombre}!!!")

#Función lambda volcada sobre una variable:
saludo = lambda name : print(f"Hola {name}!!!")

saluda("Aitor")
saludo("Borja") #Uso de la variable con función lambda.


#Pintar el resultado de sumarle 10 a cada uno de los números de la lista:
numeros = [10, 43, 2, 65, 2, 67, 34]

#Expresion lambda con un parámetro "n" donde a "n" le sumamos 10:
sumar10 = lambda n : n + 10
#Expresion lambda donde sumamos los parámetros "n1" y "n2" (dos parámetros):
sumarVar = lambda n1, n2 : n1 + n2

print(sumar10(numeros[1]))
print(sumarVar(numeros[3], numeros[4]))

#Incluida la expresión lambda en un for para sumar 10 en todos los elementos de la lista:
for e in numeros:
    print(sumar10(e))
#Incluida la expresión lambda en un for para sumar 2 en todos los elementos de la lista:
for e in numeros:
    print(sumarVar(e, 2))


#TABLA DE MULTIPLICAR:
numeroIn = int(input("Dime un número: ")) #Variable del input -> numIn.

def multiplicador(num): #La fucnión tiene el argumento: num. DONDE VA LA VARIABLE INPUT.
    return lambda a : a * num #Retorna una función lambda con la operación multiplicar: argumento "a" * el parámetro "num" (ocupado por la variable input)
      
def calcular(formula): #En el argumento (formula), METEMOS LA FUNCIÓN LAMBDA con la operación A * INPUT.
    for indice in range(1, 11): #Iteración INDICE: recorre los números del 1 al 10.
        print(formula(indice)) #Pintar LA FUNCIÓN LAMBDA CON EL ÍNDICE COMO PARÁMETRO (A) -> INDICE (A) * INPUT.

calcular(multiplicador(numeroIn)) #1. INPUT -> 2. FUNCIÓN LAMBDA -> 3. ITERACIÓN DE LA FUNCIÓN LAMBDA (INDICE -> 10 VECES).


#De esta manera podemos calcular operaciones diferentes dentro de la función de iteración (calcular):
def divisor(num):
    return lambda a : a / num

calcular(divisor(numeroIn))
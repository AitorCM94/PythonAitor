#Función normal:
def saluda(nombre):
    print(f"Hola {nombre}!!!")

#Función lambda volcada sobre una variable:
saludo = lambda name : print(f"Hola {name}!!!")

saluda("Aitor")
saludo("Borja") #Uso de la variable con una función lambda.


#Pintar el resultado de sumarle 10 a cada uno de los números de la lista:
numeros = [10, 43, 2, 65, 2, 67, 34]

#Expresion lambda con un parámetro "n" donde a "n" le sumamos 10:
sumar10 = lambda n : n + 10
#Expresion lambda donde sumamos los parámetros "n1" y "n2":
sumarVar = lambda n1, n2 : n1 + n2

print(sumar10(numeros[1]))
print(sumarVar(numeros[3], numeros[4]))

#Incluida la expresión lambda en un for para sumar 10 en todos los elementos de la lista:
for e in numeros:
    print(sumar10(e))
#Incluida la expresión lambda en un for para sumar 10 en todos los elementos de la lista:
for e in numeros:
    print(sumarVar(e, 2))


#TABLA DE MULTIPLICAR:
def func(num):
    return lambda a : a * num #La fucnión nos retorna una función lambda con 1 argumento (parámetro).

multiplicador = int(input("Dime un número: "))
for n in range(1, 11):
    print(f"{n} x {multiplicador} = {func(n)(multiplicador)}") #Utiliza la función lambda (retornada por func) con "n" (a) y el input (num).

#FALTA: DEFINICIÓN COMO FUNCIÓN PARA HACER DISTINTAS OPERACIONES -> 3:20h
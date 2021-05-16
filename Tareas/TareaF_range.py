#Muestra las siguientes secuencias de número utilizando un FOR:
"""
#del 1 al 100:
for n in range(1, 101):
    print(n, end=' ')

#del 200 al 190:
for n in range(200, 189, -1):
    print(n, end=' ')

#del 10 a 10000 de 100 en 100:
for n in range(10, 10000, 100):
    print(n, end=' ')

#los números impares del 51 al 91
for n in range(51, 91, 2):
    print(n, end=' ')

#los multiplos de 5 del 40 al 30
for n in range(40, 29, -5):
    print(n, end=' ')

#tabla de multiplicar de PI
import math
for n in range (1, 11):
    print(n * math.pi)
"""
#del 10 al 20 sumado con el anterior
suma = 1 #NO FUNCIONA
for n in range(10, 20, suma):
    suma += n
    print(n, end=' ')

#del 20 al 10 multimplicando del 5 a 8, utilizando dos FOR
for n in range(20, 10, -1):
    for i in range(5, 8):
        print(f"{i}", end=' ')
    print(f"({n})", end=' ')
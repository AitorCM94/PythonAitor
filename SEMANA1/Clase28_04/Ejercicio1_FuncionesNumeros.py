#Funcion que te muestre todos los números entre un número y otro.
def muestraNumeros (inicio, fin, incremento):
    if (inicio > fin):
        incremento = incremento * -1 #Pasa el número del incremento a negativo para que vaya restando.
        fin = fin - 1 #Para que muestre el último número (no funciona).
    for num in range(inicio, (fin + 1), incremento): #Para que muestre el último, si no se queda en el número anterior al especificado.
        print(num)

muestraNumeros(100, 10, 1)
"""
Generamos un numero aleatorio.
Preguntar al operador un numero.
Decir si el operador ha acertado o no.
Si no ha acertado, hacer que vuelva a escribir un numero hasta que acierte.
"""
import random

numero1 = random.randint(1, 10)
numero2 = 0 #Creamos una nueva variable y le ponemos el valor 0. Mientras el valor de las dos variables no coincida podemos hacer que se ejecute el while.

while(numero1 != numero2): #LA CONDICIÓN ES LO MAS IMPORTANTE
    numero2 = int(input("Dime un numero: ")) #Preguntamos por el número.
    if (numero1 != numero2):
        print("No has acertado")
        if(numero1 < numero2):
            print(f"Te has pasado por {numero2 - numero1} numeros.")
        else:
            print(f"Te faltan {numero1 - numero2} numeros.")
    else:
        print("Has acertado")

#CONDICIONES PARA WHILE
# while (True): #Si la condición siempre se cumple, deveremos añadir un break en algún momento para salir del while.
#   print("")
#   break
# while (numero1 == numero1):
#   print("")
#   break
# while (numero1): #Una variable normal es True cuando contiene un valor / Una booleana es True cuando contiene True.
#   print("")
#   break
#
# acertado = False #Añadir una variable en la que el valor de esta nos marque la condición para el while. De modo que si cambia salimos del while.
# while (acertado == False):
#   print("")
#   acertado = True
import random
#while dime un numero, si es es numero has acertado, si no seguimos ejecutando

numero1 = random.randint(1, 10)
numero2 = 0

while(numero1 != numero2): #LA CONDICIÓN ES LO MAS IMPORTANTE
    numero2 = int(input("Dime un numero: "))
    if (numero1 != numero2):
        print("No has acertado")
        if(numero2 < numero2):
            print(f"Te faltan {numero2 - numero1} numeros.")
        else:
            print(f"Te has pasado por {numero1 - numero2} numeros.")
    else:
        print("Has acertado")
    
    
    
    #(True)
    #break

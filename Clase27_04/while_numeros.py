import random
#while dime un numero, si es es numero has acertado, si no seguimos ejecutando

numero1 = random.randint(1, 2)
numero2 = 0

while(numero1 != numero2): #LA CONDICIÓN ES LO MAS IMPORTANTE
    numero2 = int(input("Dime un numero: "))
    if (numero1 != numero2):
        print("No has acertado")
    else:
        print("Has acertado")
    
    
    
    #(True)
    #break

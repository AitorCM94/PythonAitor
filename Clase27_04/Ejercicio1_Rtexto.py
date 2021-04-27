"""
1. Preguntar al operador una frase
2. Preguntar al operador una letra
3. Mostrar por pantalla cuantas veces aparece la letra en la frase
4. Tenemos que usar un WHILE
"""
"""
#Propio: 
frase = input("Escribe la frase: ")
letra = input("Escribe una letra: ")

index=0
contador=0
while (index < len(frase)):
    if (frase[index] == letra):
        contador += 1
    index += 1
print(f"La letra '{letra}' se repite {contador} veces.")
"""
"""
#David:
frase = input("Escribe la frase: ")
letra = input("Escribe una letra: ")
#Pone condiciones a los input:
if(len(frase) < 2):
    print("Ingresa una frase.")
elif(len(letra) > 1 or letra == " "):
    print("Ingresa una sola letra")
else:
    contador, i = 0, 0 #Declaración de dos variables juntas -> Separadas por la coma.

    while(i < len(frase)):
        if(frase[i].lower() == letra.lower()): #Las pone en minúscula para que las cuente todas.
            contador += 1
        i += 1
    print(f"La letra '{letra}' se repite {contador} veces.")
"""
#Borja:
frase = input("Escribe una frase: ")
letra = "" #Variable vacía
#Primero pregunta por la variable letra y le pone una condición, que sea igual a uno para poder seguir.
while (len(letra) != 1):
    letra = input("Escribe una letra: ")
    if (len(letra) != 1):
        print(f"{letra}, no es válido.")
#El resto es = que en el mio:
index = 0
contador= 0
while (index < len(frase)):
    if (frase[index] == letra):
        contador += 1
    index += 1
print(f"La letra '{letra}' se repite {contador} veces.")
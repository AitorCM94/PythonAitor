numero = 100

#Pregunta un número al operador y muestra el mensaje los siguientes mensajes:
inNum = int(input("Número: "))

#Correcto si el valor coincide con el contenido en la variable numero:
if (inNum == numero):
    print("Correcto")

#Bajo si el valor es inferior al contenido en la variable numero:
elif(inNum < numero):
    print("Bajo")

#Alto si el valor es superior al contenido en la variable numero:
#Añade la palabra Demasiado si la diferencia entre el valor y contenido de la variable numero es de 25 o más:
else:
    if((inNum - numero) > 25):
        print("Demasiado")
    else:
        print("Alto")

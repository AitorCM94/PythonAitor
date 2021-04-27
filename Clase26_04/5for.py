#Recorrer listas
citricos = ["limón", "naranja", "pomelo", "líma"] #Variable lista.
for fruta in citricos:
    print(f"Elemento: {fruta}.") #Pinta cada elemento (fruta) de la variable lista.

#Calcular el número de elementos de la lista:
print(f"Número de cítricos: {len(citricos)}")

##################################################################################################

#Codificar contadores
for numero in range(7): #Con range() le estamos indicando el [stop] -> en que iteración parar
    print(f"Contador: {numero}") #Pinta la posición de cada elemento de la lista.


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Juntamos todo lo anterior:
#POSICIÓN DE CADA ELEMENTO DE LA LISTA:
for numero in range(len(citricos)): # Repetir la iteración hasta que se pase por cada uno de los elementos de la lista citricos. 
    print(f"P: {numero} -> {citricos[numero]}") #Pintamos el elemento numero (en este caso marcado por la función contador range()). Esto nos da la posición.
                                                #Y pintamos el elemento de cada posición de la variable lista cítricos.

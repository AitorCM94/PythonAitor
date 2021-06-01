import statistics

#TUPLAS
continentes = ("Europa", "América", "África", "Asia", "Oceanía", "Antártida")
codigos = (17, 20, 23, 13, 45, 10, 8, 45)

print(codigos) #Pinta la Tupla.
print(codigos[4]) #Pinta el contenido de la posición 4.
print(list(codigos)) #Pinta la Tupla como una lista.
print(list(enumerate(codigos))) #Pinta la Tupla como una lista con el contenido y la posición delos elementos.

#Funciones de agregación (operadores): #También sirven para las listas.
print(max(codigos)) #Pinta el elemento más alto.
print(min(codigos)) #Pinta el elemento más bajo.
print(sum(codigos)) #Suma todos los elementos de la Tupla.
print(statistics.mean(codigos)) #Promedio de los elementos de la Tupla

#CONJUNTOS
set1 = {"java", "python", "android", "java"}
print(set1)

set1.add("ruby")
print(set1)
set1.discard("android") 
print(set1)

print(len(set1))
for s in set1:
    print(s)

#DICCIONARIOS
dicc = {"red":"rojo", "blue":"azul", "green":"verde",}
print(dicc)
print(dicc["red"]) #Pinta el elemento que corresponde a la clave indicada.
print(dicc.get("ddd")) #Para acceder a los valores a través de la clave y saber si esa clave existe
print(len(dicc))

dicc["black"] = "negro" #Añadimos un elemento (negro) con su clave (black) al diccionario
print(dicc)
dicc.pop("blue") #Elimina un elemento especificando la clave (blue).
print(dicc)

for clave in dicc:
    print(clave, "->", dicc[clave]) #Ifual que las listas, pero te muestra la clave que hayas puesto en lugar de la posición.

#Funciones que tenemos que PARSEAR para que se muestren
#dicc.keys #Muestra las claves
#dicc.values #Muestra los valores

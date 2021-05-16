cadena = "Hola mundo !!"

#A1. Pregunta el nombre de Operador y muestra un saludo incluyendo el contenido de la variable.cadena.
inNombre = input("Nombre: ")
saludo = f"{cadena} Me llamo {inNombre} !!"
print(saludo)

#A2. Muestra el saludo, en mayúsculas, minúsculas y con la letra de cada palabra en mayúsculas.
mayusculas = print(saludo.upper())
minusculas = print(saludo.lower())
lista = saludo.split(" ")
#print(lista)
for p in lista:
    print(p.capitalize(), end=' ')
#mayMin = print(lista[0].capitalize(), lista[1].capitalize(), lista[2], lista[3].capitalize(), lista[4].capitalize(), lista[5].capitalize(), lista[6])

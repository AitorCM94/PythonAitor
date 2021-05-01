listaClientes = [] #Variable donde vamos a volcar todo el texto del fichero, convertido ya en una lista.

#2. Funciones para abrir el fichero y leerlo (línea por línea):
lecturaFichero = open(path).readlines() #Variable de tipo list.


print(type(lecturaFichero))
print(lecturaFichero)


##############3



for linea in ():
    fichero = linea.split(",") #con el split transformamos el texto en una lista.
    
    if (linea[0].isdigit() == True): #Preguntar si linea posición 0 es un digito.
        #clientes.append(Cliente(fichero[1], fichero[2], fichero[7]))
        cliente = Cliente(fichero[1].strip(), fichero[2].strip(), fichero[7].strip) #Creamos una variable cliente temporal. #Quitar espacios en blanco.
        clientes.append(cliente) #añadir la información en la variable

fichero.close()
print(f"{len(cliente)} clientes importados.")


#resultado = list(filter(lambda x : x.Id))
    #print(linea)
    #print(linea[2])
    #print(fichero)
    #print(fichero[2])
    #for n in fichero: #pinta cada uno de los elementos de la colección.
    #    print(n)
    #break #Para hacerlo solo con la primera línea.
    
#for c in clientes:
#    print(c.Nombre)

#Definición de la función que te permite buscar por el identificador de cada cliente.
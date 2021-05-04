import pickle #Objeto que nos permite gravar o leer en binario.

#Métodos para pasar un texto a bytes: 
bytes1 = "En un lugar de la Mancha...".encode() #Bytes
bytes2 = b"En un lugar de la Mancha..." #Bytes
bytes3 = bytes("En un lugar de la Mancha...", "utf-8") #Bytes. utf-8 -> Especifica el encoding del texto (como esta codificado).
print(type(bytes1)) #Python pinta el texto con una b delante para indicar que esta en formato de bytes.

for b in bytes3:
    print(b, end=' ') #Pinta cada caracter en formato byte. end=' ' Para que pinte en una sola línea y separados por espacios.
print("")
print(bytes3.hex()) #Representación de bytes a hexadecimal. Cada dos carácteres es la representación de uno en formato de bytes (decimal).

"""
#1. Abrimos el fichero en modo escritura, binario. Si el fichero no existe, crea uno nuevo:
fichero = open(".\\SEMANA1\\Clase29_04\\2Test.bin", "wb")
#2. Escribimos en el fichero con la función .dump:
texto = "En un lugar de la Mancha..."
pickle.dump(texto, fichero)
fichero.close()
"""
"""
#1. Abrimos el fichero en modo lectura, binario:
fichero = open(".\\SEMANA1\\Clase29_04\\2Test.bin", "rb")
#2. Leemos la información del fichero con la función .load:
texto = pickle.load(fichero)
#print(texto)
fichero.close()
"""
"""
#Podemos gravar la información en formato bytes o hexadecimal en un fichero de texto normal:
fichero = open(".\\SEMANA1\\Clase29_04\\2Test.txt", "wt")
fichero.write(bytes3.hex())
fichero.close()
"""
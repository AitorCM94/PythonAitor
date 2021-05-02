
"""
#Métodos para pasar un texto a bytes. 
bytes1 = "En un lugar de la Mancha...".encode() #Bytes
bytes2 = b"En un lugar de la Mancha..." #Bytes
bytes3 = bytes("En un lugar de la Mancha...", "utf-8") #Bytes
print(type(bytes1)) #Python pinta el texto con una b delante para indicar que esta en formato de bytes.

for b in bytes3:
    print(b, end=' ') #Pinta cada caracter en formato byte.
"""

#MODO BINARIO:
import pickle
"""
#1. Abrimos el fichero en modo escritura, binario. Si el fichero no existe, crea uno nuevo:
fichero = open(".\\SEMANA1\\Clase29_04\\2Test.bin", "wb")
#2. Escribimos en el fichero con la función .dump:
texto = "En un lugar de la Mancha..."
pickle.dump(texto, fichero)
"""
"""
#1. Abrimos el fichero en modo lectura, binario:
fichero = open(".\\SEMANA1\\Clase29_04\\2Test.bin", "rb")
#2. Leemos la información del fichero con la función .load:
texto = pickle.load(fichero)
#print(texto)
"""
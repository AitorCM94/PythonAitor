numero0 = "3"
numero1 = 2
numero2 = 100

try:
    print(type(numero0))
    if(type(numero0) is not int):
        raise Exception("La variable no es numérica.", "1004958AA") #Generamos una excepción.
    
    numero3 = numero2 / numero1
    print(f"Número 3: {numero3}")

except ZeroDivisionError:
    print("No se puede dividir entre 0.")

except Exception as TypeException: #Guardamos la excepción dentro de la variable TypeException.
    print("Mensaje: " + TypeException.args[0]) #Mostramos el texto del error.
    print("Código: " + TypeException.args[1]) #Mostramos el código del error.

except:
    print("Error")
else:
    print("Finalizado correctamente el try.")
finally:
    print("Finalizado try/except.")
print("Fin del programa")
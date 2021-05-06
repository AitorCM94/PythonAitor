import math
#B1. Pregunta un número al operador y muestra el resultado de multiplicarlo por PI. Utiliza la constante "math.pi" y recuerda incluir "import math".
#B2. Muestra la raíz cuadrada del mismo número.
#B3. Muestra el arco coseno del mismo número.

inNum = float(input("Número entre 0 y 1: "))

if (inNum < 1 and inNum > 0):
    mult = print(f"{inNum} x π = {inNum*math.pi:2.4f}")
    raiz2 = print(f"Raíz cuadrada: {math.sqrt(inNum):2.4f}")
    acos = print(f"Arco coseno: {math.acos(inNum):2.4f}")
else:
    print("No es correcto.")
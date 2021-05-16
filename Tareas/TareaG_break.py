#G1. Pregunta al operador cualquier cosa.

#G2. Muestra por Simón dice xxxxxxxxx incluyendo la respuesta del operador

#G3. Esta secuencia de pregunta/mostrar en pantalla se repite hasta que el operado responde fin:

texto = ""

while (texto != "fin"):
    texto = ""
    texto = input("Escribe: ")
    print(f"Simón dice {texto}")

"""
dentro del while un if que dentro tenga un break.
"""
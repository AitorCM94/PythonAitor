lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]


#D1. Pregunta al operador su DNI sin letra.
dniInp = input(f"Número del DNI sin letra: ")

#D2. Calcula el resto de dividir el número del DNI entre 23.
resto = int(dniInp) % 23

#D3. Muestra el DNI con la letra. El resto de la división representa la posición de la letra del DNI en lista.
print(f"DNI: {dniInp}{lista[resto]}")



#try:
"""
if ((len(dniInp) == 8) and (dniInp.isdigit() != True)): # and // No funciona el and
    print("funciona")
"""



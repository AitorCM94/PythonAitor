#D1. Pregunta al operador su DNI sin letra.

#D2. Calcula el resto de dividir el número del DNI entre 23.

#D3. Muestra el DNI con la letra. El resto de la división representa la posición de la letra del DNI en lista.
lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

#try:
dniInp = input(f"Número del DNI sin letra: ")

numDNI = int(dniInp)

resto = numDNI % 23

print(f"DNI: {numDNI}{lista[resto]}")

#if ( == int):
#    resto = dniNoL % len(dn)
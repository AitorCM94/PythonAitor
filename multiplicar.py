numoFor = input("La tabla del: ")

if(numFor.isdigit() == True):
    print()
    for numero in range (11):
        print(f"{numFor} x {numero:2.0f} = {numFor*numero:2.0f}")
else:
    print(f"{numero}, no es un número.")
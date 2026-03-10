nombre = input("Veuillez renseigner un nombre ")
nombre = int(nombre)

factoriel = 1
if nombre == 0:
    print("le factoriel de {nombre} est 1")
elif nombre < 0:
    print("Veuillez saisir un nombre positif")
else:
    for i in range(1, nombre + 1):
        factoriel = factoriel * i
    print(f"le factoriel de {nombre} est {factoriel}")

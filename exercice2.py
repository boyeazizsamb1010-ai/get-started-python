nombre1 = float(input("Entrer le nombre 1 : "))
nombre2 = float(input("Entrer le nombre 2 : "))
nombre3 = float(input("Entrer le nombre 3 : "))
if nombre1 > nombre2 and nombre1 > nombre3:
    print(f"Le maximum est : {nombre1}")
elif nombre2 > nombre1 and nombre2 > nombre3:
    print(f"Le maximum est : {nombre2}")
else:
    print(f"Le maximum est : {nombre3}")
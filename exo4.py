Taux_conversion = 655.957

montant_convertir = float(input("Veuillez renseigner le montant: "))

devise = input("Veuillez renseigner la devise(E pour Euro et C pour Cfa): ")

if devise == "E":
    montant_converti = montant_convertir * Taux_conversion
    print(f"{montant_convertir} Euro = {montant_converti} Cfa")

elif devise == "C":
    montant_converti = montant_convertir / Taux_conversion
    print(f"{montant_convertir} Cfa = {montant_converti}")

else:
    print("Error !")
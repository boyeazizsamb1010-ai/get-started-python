numero_telephone = int(input("Veuillez renseigner le numero de téléphone: "))

code_operateur = numero_telephone // 10000000

if code_operateur == 70:
    print("Votre opérateur est Expresso")

elif code_operateur == 75:
    print("Votre opérateur est Promobile")

elif code_operateur == 76:
    print("Votre opérateur est Free")

elif (code_operateur == 77) or (code_operateur == 78):
    print("Votre opérateur est Orange")

else:
    print("Votre opérateur n'existe pas")
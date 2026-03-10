CODE_PIN = 1234
pine = int(input("Entrer le mot de passe : "))

while pine != CODE_PIN:
    print("mot de passe incorrecte !")
    pine = int(input("Entrer a nouveau le mot de passe : "))
print("Telephone dévérouillé !")

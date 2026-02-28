a = float(input("Veuillez renseigner a: "))
b = float(input("Veuillez renseigner b: "))
c = float(input("Veuillez renseigner c: "))

if a > b and a > c:
    print(f"Le maximum est {a}")
elif b > a and b > c:
    print(f"Le maximum est {b}")
else:
    print(f"Le maximum est {c}")

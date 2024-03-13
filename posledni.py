n = int(input("Zadejte počet čísel: "))
cisla = []

for i in range(n):
    cisla.append(int(input("Zadejte číslo: ")))

if n > 0:
    posledni_cislo = cisla[-1]

    pocet_rovnajicich_se = cisla[:-1].count(posledni_cislo)

    print("Počet čísel rovnajících se poslednímu číslu:", pocet_rovnajicich_se)
else:
    print("Nezadali jste žádná čísla.")
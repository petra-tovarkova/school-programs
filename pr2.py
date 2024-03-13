
seznam = []

#úkol a)
n = int(input("Zadejte počet předmětů:"))
for i in range(n):
    predmet = []
    nazev = input("Zadejte název předmětu:")
    predmet.append(nazev)

    zkratka = input("Zadejte zkratku předmětu:")
    while not (3 <= len(zkratka) <= 4):
        zkratka = input("Zadaná hodnota neodpovídá požadavkům. Zadejte znovu:")
    else:
        predmet.append(zkratka)

    hodiny = int(input("Zadejte počet hodin předmětu za týden:"))
    while not (1 <= hodiny <= 7):
        hodiny = int(input("Zadaná hodnota neodpovídá požadavkům. Zadejte znovu:"))
    else:
        predmet.append(hodiny)

    prumer = float(input("Zadejte průměr známek třídy(použijte tečku místo čárky pro desetinné číslo):"))
    while not (1 <= prumer <= 5):
        prumer = float(input("Zadaná hodnota neodpovídá požadavkům. Zadejte znovu:"))
    else:
        predmet.append(prumer)
        seznam.append(predmet)

print("Seznam předmětů:")
for i in range(n):
    print(seznam[i])

#úkol b)
nejmene = 6
for i in range(n):
    if seznam[i][3] < nejmene:
        nejmene = seznam[i][3]
print("Předměty s nejlepším průměrem:")
for i in range(n):
    if seznam[i][3] == nejmene:
        print("Název:",seznam[i][0],", zkratka:", seznam[i][1])

#úkol c)
prumer_nizsi_hodiny = 0
prumer_vyssi_hodiny = 0
pocet_nizsi_hodiny = 0
pocet_vyssi_hodiny = 0

for i in range(n):
    if 0 <=  seznam[i][2] <= 2:
        prumer_nizsi_hodiny += seznam[i][3]
        pocet_nizsi_hodiny += 1
    elif seznam[i][2] >= 3:
        prumer_vyssi_hodiny += seznam[i][3]
        pocet_vyssi_hodiny += 1
    elif seznam [i][2] == 0:
        print("Zadaná hodinová dotace nebyla zadaná správně.")
        
prumer_nizsi_hodiny = prumer_nizsi_hodiny / pocet_nizsi_hodiny
prumer_vyssi_hodiny = prumer_vyssi_hodiny / pocet_vyssi_hodiny

if prumer_nizsi_hodiny > prumer_vyssi_hodiny:
    print("Průměr známek z předmětů s nižší hodinovou dotací je lepší.")
elif prumer_nizsi_hodiny < prumer_vyssi_hodiny:
    print("Průměr známek z předmětů s vyšší hodinovou dotací je lepší.")
else:
    print("Průměr známek z předmětů s nižší hodinovou dotací je stejný jako z předmětů s vyšší hodinovou dotací.")

#úkol d)
nejvyssi_hodinova_dotace = 0
for i in range(n):
    if seznam[i][2] > nejvyssi_hodinova_dotace:
        nejvyssi_hodinova_dotace = seznam[i][2]

print("Nejvyšší hodinová dotace je", nejvyssi_hodinova_dotace, "u předmětů:")
for i in range(n):
    if seznam[i][2] == nejvyssi_hodinova_dotace:
        print(seznam[i][0])
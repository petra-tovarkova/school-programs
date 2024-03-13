n = int(input("Zadejte počet hodnot:"))
seznam = []
prum = 0

for i in range(n):
    cislo = int(input("Zadejte číslo:"))
    prum = prum + cislo
    seznam.append(cislo)

prum = prum/n
print("Podprůměrná čísla:")

for cislo in seznam:
    if cislo < prum:
        print(cislo)
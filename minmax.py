cisla = []

while True:
    vstup = input("Zadejte číslo nebo stiskněte ENTER pro ukončení: ")

    if not vstup:
        break

cislo = int(vstup)
cisla.append(cislo)

for cislo in cisla:
    if cislo > max:
        max = cislo
    else:
        max = max

for cislo in cisla:
    if cislo < min:
        min = cislo
    else:
        min = min
   
    print("Největší číslo je", min)
    
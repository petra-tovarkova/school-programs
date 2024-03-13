seznam_cisel = []

while True:
    vstup = input("Zadejte číslo nebo stiskněte ENTER pro ukončení: ")

    if not vstup:
        break

cislo = int(vstup)
seznam_cisel.append(cislo)
    
if seznam_cisel:
    soucet = sum(seznam_cisel)
    prumer = soucet / len(seznam_cisel)
    print("Aritmetický průměr zadaných čísel je:",prumer)
else:
    print("Seznam čísel je prázdný.")
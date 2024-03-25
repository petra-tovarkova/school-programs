#test sk.B, Petra Továrková
#úkol 2
seznam = []
n = int(input("Zadejte počet studentů: "))

for i in range(n):
    radek = []
    prijmeni = input("Zadejte příjmení:")
    radek.append(prijmeni)
    obor = input("Zadejte obor studia:")
    radek.append(obor)
    semestr = int(input("Zadejte semestr:"))
    if semestr < 0:
        print("Zadejte znovu:")
    else:
        radek.append(semestr)
    seznam.append(radek)
                            
print("Seznam studentů:")
for radek in seznam:
    print(radek)

print("Studenti studující 3. a 4. semestr:")
for radek in seznam:
    if (radek[2] == 3) or  (radek[2] == 4):
        print(radek[0], radek[1])


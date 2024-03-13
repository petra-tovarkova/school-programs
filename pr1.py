seznam = []
prm = 0
prf = 0
n = int(input("Zadejte počet studentů:"))

for i in range(n):
    student = []
    jm = input("Zadejte jméno studenta:")
    student.append(jm)

    t = input("Zadejte třídu:")
    student.append(t)

    mat = int(input("Zadejte známku z matematiky:"))
    student.append(mat)
    prm += mat

    fyz = int(input("Zadejte známku z fyziky:"))
    student.append(fyz)
    prf += fyz
    seznam.append(student)

print("Seznam studentů:")
for i in range(n):
    print(seznam[i])

# úkol a)
prm /= n
for i in range(n):
    if seznam[i][2] < prm:
        print("Žáci nadprůměrní z matematiky:",seznam[i][0]," ",seznam[i][2])

# úkol b)
for i in range(n):
    if seznam[i][3] == 1:
        print("Žáci s jedničkou z fyziky:",seznam[i][0], " " ,seznam[i][1])

# úkol c)
prf /= n
if prm < prf:
    print("Lepší je průměr z matematiky o", round(prf-prm,2) , "stupně.")

elif prf < prm:
    print("Lepší je průměr z fyziky o", round(prm-prf,2) , "stupně.")

else:
    print("Průměr známek z matematiky a fyziky je stejný.")


#test sk.B, Petra Továrková
#úkol 1

matice = []
n = int(input("Zadejte rozměr matice: "))

for i in range(n):
    radek = []
    for j in range(n):
        print("Zadejte prvek [", i+1, ",", j+1, "] matice:", end= " ")
        x = int(input())
        radek.append(x)
    matice.append(radek)

print("Prvky matice:")
for radek in matice:
    print(radek)


maximum = matice[0][0]
souradnice = (0,0)

for i in range(n):
    for j in range(n):
        if matice[i][j] > maximum:
            maximum = matice[i][j]
            souradnice = (i,j)

for i in range(n):
    for j in range(n):
        if matice[i][j] == maximum:
            matice[i][j] = 0    

print("Prvky výsledné matice:")
for radek in matice:
    print(radek)


















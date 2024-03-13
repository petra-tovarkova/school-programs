n = int(input("Zadejte rozměr matice n: "))
matice = []

print("Zadejte prvky matice po řádcích:")
for i in range(n):
    radek = []
    for j in range(n):
        print("Zdejte prvek [", i+1, ",", j+1, "] matice:", end= " ")
        x = int(input())
        radek.append(x)
    matice.append(radek)

print("Prvky matice:")
for radek in matice:
    print(radek)

symetricka = True
for i in range(n):
    for j in range(n):
        if matice[i][j] != matice[j][i]:  
            symetricka = False
            break
    if not symetricka:
        break

if symetricka:
    print("Matice je symetrická podle hlavní diagonály.")
else:
    print("Matice není symetrická podle hlavní diagonály.")
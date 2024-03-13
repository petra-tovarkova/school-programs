matice = []
minima = []
maxima = []

n = int(input("Zadejte rozměr matice:"))

for i in range(n):
    radek = []
    for j in range(n):
        print("Zadejte prvek [", i+1, ",", j+1,"] matice:", end=" ")
        x = int(input())
        radek.append(x)
    matice.append(radek)
    minima.append(min(radek))
    maxima.append(max(radek))
    
print("Zadaná matice:")

for i in range(n):
    for j in range(n):
        print(matice[i][j], end=" ")

    print()
print()

mn = min(minima)
mx = max(maxima)
print("Nejmenší prvek je", mn," a největší prvek je", mx)
print("Matice se zaměněnými nejmenšími a nejvěšími prvky:")

for i in range(n):
    for j in range(n):
        if matice[i][j] == mn:
            matice[i][j] = mx

        elif matice[i][j] == mx:
            matice[i][j] = mn
        print(matice[i][j],end = " ")
    print()
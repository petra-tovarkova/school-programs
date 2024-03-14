matice = []
matice2 = []
n = int(input("Zadejte rozměr matice:"))
m = int(input("Zadejte rozměr matice:"))

for i in range(m):
    radek = []
    for j in range(n):
        print("Zadejte prvek [", i+1, ",", j+1,"] matice:", end=" ")
        x = int(input())
        radek.append(x)
    matice.append(radek)

print("Zadaná matice:")

for i in range(n):
    for j in range(n):
        print(matice[i][j], end=" ")

    print()
print()

print("Matice se součty řádků:")
for i in range(n):
    soucet = sum(matice[i])
    radek.append(soucet)
    matice2.append(radek)
for j in range(n):
    print(matice[i][j], end=" ")
print()
print()

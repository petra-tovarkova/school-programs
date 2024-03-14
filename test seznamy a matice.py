n = int(input("Zadejte rozměr matice:"))
m = int(input("Zadejte rozměr matice:"))
matice = []

for i in range(m):
    radek = []
    for j in range(n):
        print("Zadejte prvek matice [",i+1, ",", j+1, end=" "])
        x = int(input())
        radek.append(x)
    matice.append(radek)

print("Zadaná matice:")

for i in range(n):
    for j in range(n):
        print(matice[i][j], end=" ")

    print()
print()

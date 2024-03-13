matice = []
n = int(input("Zadejte rozměr matice:"))

for i in range(n):
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
print("Matice s prvky uspořadanými v řádcích sestupně:")
for i in range(n):
    matice[i].sort(reverse=True)
    for j in range(n):
        print(matice[i][j], end=" ")
    print()
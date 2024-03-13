matice = []
n = int(input("Zadejte první rozměr matice: "))
m = int(input("Zadejte druhý rozměr matice: "))

for i in range(n):
    radek = []
    for j in range(m):
        print("Zadejte prvek[", i+1, "," ,j+1, "] matice:", end=" ")
        x = int(input())
        radek.append(x)
    matice.append(radek)
print("Zadaná matice: ")
for i in range(n):
    for j in range(m):
        print(matice[i][j], end=" ")
    print()
print()

maximum = matice[0][0]
souradnice = (0, 0)
                 
for i in range(n):
    for j in range(m):
        if matice[i][j] > maximum:
                 maximum = matice[i][j]
                 souradnice = (i, j)

print("Maximum matice je:", maximum, "a jeho souřadnice jsou:", souradnice[0] + 1, souradnice[1] + 1)
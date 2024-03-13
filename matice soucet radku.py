matice = []
n = int(input("Zadejte rozměr matice: "))

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

for i in range(n):
    s = [0]*n
    for radek in matice:
        for i in range(n):
            s[i] += radek[i]

print("Součty prvků v jednotlivých sloupcích:")
for soucet in s:
    print(soucet)
n = int(input("Zadejte počet čísel:"))
s = 0
for i in range(n):
    n = float(input("Zadejte číslo:"))
    s = s + n

p = s/n
print("Aritmetický průměr je:", p)
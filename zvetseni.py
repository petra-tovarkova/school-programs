import random
n = int(input("Zadejte počet čísel v seznamu:"))
seznam = []
for i in range(n):
    x = random.randint(0,20)
    seznam.append(x)
print("Vygenerovaný seznam je:",seznam)

for i in range(n):
    seznam[i] += i + 1
print("Zvětšený seznam:",seznam)

import random
seznam = []
pomocny = []
for i in range(15):
    x = random.randint(0,30)
    seznam.append(x)
    pomocny.append(x)
print("Vygenerovaný seznam je:", seznam)

c = int(input("Zadej číslo jehož násobek chceš vymazat:"))
for i in range(15):
    if pomocny[i] % c == 0:
        seznam.remove(pomocny[i])
print("Seznam bez násobků čísla", c,"je:",seznam)
import random
mnozina = []

for i in range(10):
    x = random.randint(0,9)
    print(x)
    if not x in mnozina:
        mnozina.append(x)

print("Moje množina je:", mnozina)
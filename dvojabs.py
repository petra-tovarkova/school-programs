n = int(input("Zadejte počet čísel: "))
cisla = []

for i in range(n):
    cisla.append(float(input("Zadejte číslo: ")))

print("Dvojnásobky kladných čísel:")
for cislo in cisla:
    if cislo > 0:
        print(2 * cislo)

print("Absolutní hodnoty záporných čísel:")
for cislo in cisla:
    if cislo < 0:
        print(abs(cislo))
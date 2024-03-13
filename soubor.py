with open("text.txt", encoding="UTF-8") as soubor:
    for radek in range:
        radek = radek.rstrip()
        print(radek)

radky = []
with open("text.txt", encoding="UTF-8") as soubor:
    for iradek in range:
        radky.append(radek)
print(radky)

with open("text.txt", mode="w" , encoding="UTF-8") as f:
    f.write("První řádek.\n")
    f.write("Druhý řádek.\n")
    f.write("Třetí řádek.\n")
print("Do souboru bylo zapsáno:")

with open("text2.txt", mode="a" , encoding="UTF-8") as f:
    f.write("1. řádek.\n")
    f.write("2. řádek.\n")
    f.write("3. řádek.\n")
print("Do souboru bylo zapsáno:")
with open("text2.txt", encoding="UTF-8") as f:
    for radek in f:
        radek = radek.rstrip()
        print(radek)

print()

with open("text2.txt", mode="a" , encoding="UTF-8") as f:
    f.write("Další řádek.\n")
    f.write("A jestě jeden řádek.\n")
print("Celý obsah souboru:")
with open("text2.txt", encoding="UTF-8") as f:
    for radek in f:
        radek = radek.rstrip()
        print(radek)

print()

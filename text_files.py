with open ("Dokument.txt", encoding="utf-8") as file:
    text = file.read()
slova = text.split
znaky = ",.:!?"
cslova = []
for slovo in slova:
    if slovo[-1] in znaky:
        slovo = slovo[:len(slovo)-1]
    cslova.append(slovo)
    slovaa = []
    for slovo in cslova:¨
    if ()
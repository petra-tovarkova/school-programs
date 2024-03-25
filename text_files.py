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
    for slovo in cslova:
        if (slovo.find("a")!=-1) or (slovo.find("A")!=-1):
            slovaa.append (slovo)

print ("Slova obsahujici pismeno a:")
print (slovaa)
print("Počet slov a pismenem a je ",len(slovaa))
print()
print("Slova delší jak 5 znaků končici na e:")
for slovo in cslova:
    if slovo[-1] == "e" and len(slovo) > 5:
        print (slovo)
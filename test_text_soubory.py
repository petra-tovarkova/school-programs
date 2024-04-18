#sk.C, Petra Továrková 3.A

with open("dokument.txt", encoding="UTF-8") as file:
    text = file.read()
    textt = text.split()

cslova = []
for slovo in textt:
    slovo.strip(".,?!")
    cslova.append(slovo)
print(cslova)


#task a)
zamena = []
for slovo in cslova:
    if len(slovo) >= 6:
        x = slovo.replace("s", "x")
        zamena.append(x)
print(zamena)


#task b)
n = 0
for slovo in cslova:
    if slovo.find("k"):
        n += 1
print(n)

with open("dokument.txt", mode="a", encoding="UTF-8") as file:
    file.write("Slov obsahujících písmeno 'k' je",n ,".\n")
    
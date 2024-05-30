with open("dokumentik.txt", encoding="utf-8") as file:
    text = file.read()
    text = text.split()
    
    cslova = []
    for slovo in text:
        slovo.strip(".,!?(-_.)'/[]")
        cslova.append(slovo)
    print(cslova)

print()
print("---------------------------------------------------------------")
print()
zamena = []
for slovo in cslova:
    if len(slovo) >= 6 and slovo.find("a") == True:
        x = slovo.replace("a" , "x")
        zamena.append(x)
print(zamena)
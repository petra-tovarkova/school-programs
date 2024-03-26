with open ("Dokument1.txt", encoding="utf-8") as file:
    text = file.read()
slova = text.split()
oznam = "."
rozkaz = "!"
tazaci = "?"
oznam_vet = 0
rozkaz_vet = 0
tazaci_vet = 0

#task a
for slovo in slova:
    if slovo[-1] in oznam:
        oznam_vet += 1
    elif slovo[-1] in rozkaz:
        rozkaz_vet += 1
    elif slovo[-1] in tazaci:
        tazaci_vet += 1

nejvice = max(oznam_vet, rozkaz_vet, tazaci_vet)
if nejvice == oznam_vet:
    print("Nejvíce je vět oznamovacích. Je jich", oznam_vet, ".")
elif nejvice == rozkaz_vet:
    print("Nejvíce je vět rozkazovacích. Je jich", rozkaz_vet, ".")
elif nejvice == tazaci_vet:
    print("Nejvíce je vět tázacích. Je jich", tazaci_vet, ".")
elif oznam_vet == rozkaz_vet:
    print("Je stejný počet vět oznamovacích a rozkazovacích. Je jich", oznam_vet, ".")
elif oznam_vet == tazaci_vet:
    print("Je stejný počet vět tazacích a oznamovacích. Je jich", tazaci_vet, ".")
elif tazaci_vet == rozkaz_vet:
    print("Je stejný počet vět tazacích a rozkazovacích. Je jich", tazaci_vet, ".")
elif tazaci_vet == rozkaz_vet == oznam_vet:
    print("Je stejný počet vět tázacích, oznamovacích i rozkazovacích vět. Je jich", oznam_vet, ".")

#task b
opraveny_text = ""
for slovo in slova:
    if "hi" in slovo or "Hi" in slovo or "hí" in slovo or "Hí" in slovo:
        nove = slovo.replace("i", "y")
        novee = nove.replace("í", "ý")
        opraveny_text += novee + " "
    else:
        opraveny_text += slovo + " "

with open("Oprava.txt", mode="a", encoding="utf-8") as f:
    f.write(opraveny_text)
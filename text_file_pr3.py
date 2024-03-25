with open ("Dokument.txt", encoding="utf-8") as file:
    text = file.read()
slova = text.split
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
    print("Nejvíce je vět oznamovacích.")
elif nejvice == rozkaz_vet:
    print("Nejvíce je vět rozkazovacích.")
elif nejvice == tazaci_vet:
    print("Nejvíce je vět tázacích.")


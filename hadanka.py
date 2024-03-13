import random

spravna_odpoved = ("budoucnost")
pokusy = 3

print("Vítejte v hádance!")
print("Máte 3 pokusy na uhodnutí správné odpovědi.")
print("Nepožívejte velká písmena ani speciální znaky.")
print()
print("Znění hadanky:")
print("Co je vždy před vámi, ale není to vidět?")
    
while pokusy > 0:
        hadane_slovo = input("Zadejte vaší odpověd: ")

        if hadane_slovo.lower() in spravna_odpoved:
            print("Skvělé! Uhodli jste správně.")
            break
        else:
            pokusy = pokusy - 1
            if pokusy > 0:
                print("Špatně! Zbývá vám" ,pokusy,"pokusy. Zkuste to znovu.")
            else:
                print("Bohužel, žádné pokusy nezbývají. Správná odpověď byla budoucnost.")


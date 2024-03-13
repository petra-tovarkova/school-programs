#Petra Továrková 3.A, test CYKLY
#Skupina F, Úloha 1

veta = input("Zadejte větu:")
obojet = 0
znaky = 0

for znak in veta:
    if znak in "bflmpsvz":
        obojet = obojet + 1

    if znak in veta:
        znaky = znaky + 1

    else:
        znak = znak - 1

print("Věta má celkem",znaky,"znaků.")
print("Věta obsahuje",obojet,"obojetných souhlásek.")

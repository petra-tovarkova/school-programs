import random

hrac_karta1 = random.randint(2, 10)
hrac_karta2 = random.randint(2, 10)
soucet = hrac_karta1 + hrac_karta2
print("Máš karty",hrac_karta1,"a",hrac_karta1,"takže máš", soucet,"bodů.")

while soucet < 21:
    odpoved = input("Chceš další kartu?")

    if odpoved == "ano":
        karta = random.randint(2,10)
        print("Dostal jsi kartu",karta)
        soucet = soucet + karta
        print("Máš", soucet,"bodů.")
    elif odpoved == "ne":
        break
    else:
        print("Nedefinováno, odpovídej ano nebo ne.")

if soucet > 21:
    print("Prohrál/a jsi. Máš více než 21 bodů! Odečti si",soucet,"bodů.")

else:
    pc_karta1 = random.randint(2,10)
    pc_karta2 = random.randint(2,10)
    pc_soucet = pc_karta1 + pc_karta2

    while (pc_soucet < 17):
        pc_karta = random.randint(2,10)
        pc_soucet = pc_soucet + pc_karta

    if (pc_soucet > 21):
        print("Gratuluji, vyhrál jsi. Počítač má", pc_soucet," bodů. Připiš si",soucet, "bodů.")

    else: 
        (soucet > pc_soucet)
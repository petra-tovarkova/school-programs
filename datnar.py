den = int(input("Zadejte den narození:"))
mesic = int(input("Zadejte mesic narození:"))
rok = int(input("Zadejte rok narození:"))
aden = int(input("Zadejte aktuální den:"))
amesic = int(input("Zadejte aktuální mesic:"))
arok = int(input("Zadejte aktuální rok:"))
print(den,".", mesic,".", rok)

datum = False
zbytek = rok%4 and rok%400

if (den<1) or (den>31):
    print("Takový den v kalendáři nenajdete!")

elif not (1<=mesic<=12):
    print("Takový měsíc v kalendáři nenajdete!")

elif (mesic == 4 or mesic == 6 or mesic == 9 or mesic == 11) and (den>30):
        print("Takové datum v kalendáři nenajdete!")

elif (mesic == 2) and (den>29):
        print("Takové datum v kalendáři nenajdete!")
#dopsat jak je to když den == 29
        
elif (rok<1900):
    print("Tak to jste asi přeživší!")

elif (rok>arok):
    print("To jste asi z budoucnosti!")

elif rok == arok:
    if (mesic>amesic):
        print("Toto datum ještě nenastalo.")

    elif (mesic == amesic) and (den>aden):
        print("Toto datum ještě nenastalo.")

    else:
        datum = True
        
else:
    print("Datum narození je relevatní!")
    datum = True

if zbytek == 0:
    print("Narodil ses v přestupném roce")

else:
    print("Nenarodil ses v přestupném roce")
        
if datum == True:
    if (3<=mesic<=5):
        print("Narodil(a) ses na jaře.")

    elif (6<=mesic<=9):
        print("Narodil(a) ses v létě.")
    
    elif (9<=mesic<=11):
        print("Narodil(a) ses na podzim.")

    else:
        print("Narodil(a) ses v zimě.")

# doplnit si presne datum rocnich obdobi ,and (den<31)

text = input("Zadejte text:")
samohlasky = 0
souhlasky = 0
cislice = 0
mezery = 0
ostatni = 0

for znak in text:
    if znak in "aáeéěiíoóuúůyýAÁEÉĚIÍOÓUŮÚYÝ":
        samohlasky = samohlasky + 1

    elif znak in "qwrtzpsdfghjklxcvbnmščřžQWRTZPSDFGHJKLXCVBNMŠČŘŽ":
        souhlasky = souhlasky + 1

    elif znak in "0123456789":
        cislice = cislice + 1

    elif znak == " ":
        mezery = mezery + 1

    else:
        ostatni = ostatni + 1

print("Text",text,"obsahuje:")
print(samohlasky,"samohlásek")
print(souhlasky,"souhlásek")
print(cislice,"cislic")
print(mezery,"mezer")
print(ostatni,"ostatních znaků")
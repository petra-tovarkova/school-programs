#task a,b,f
def caesar(string, shift):
    result = ""
    for character in string:
        if character.isdigit():
            x = (int(character) + shift) % 10
            result += str(x)
        elif ord("A") <= ord(character) <= ord("z"):
            x = ord(character) + shift
            if x - shift <= ord("Z"):
                if x > ord("Z"):
                    x -= 26
            else:  
                if x > ord("z"):
                    x -= 26
            result += chr(x)
        else:
            result += character
    return(result)

def decaesar(string, shift):
    result = ""
    for character in string:
        if character.isdigit():
            x = (int(character) - shift) % 10
            result += str(x)
        elif ord("A") <= ord(character) <= ord("z"):
            x = ord(character) - shift
            if x + shift <= ord("Z"):
                if x < ord("A"):
                    x += 26
            else:  
                if x < ord("a"):
                    x += 26
            result += chr(x)
        else:
            result += character
    return(result)

#task c
string = input("Zadejte text, který chcete (de)kódovat:")
shift = int(input("Zadejte posun:"))
choice = 0
while choice != 1 and choice != 2:
    print("1 - šifrování caesarovou šifrou.")
    print("2 - dešifrování caesarovou šifrou")
    choice = int(input("Zadejte číslo volby:"))
    if choice == 1:
        result = caesar(string, shift)
    if choice == 2:
        result = decaesar(string, shift)
print(result)

#task d
cesta = input("Zadejte cestu k textu:")
result = ""
with open(cesta, mode="r", encoding="utf-8") as file:
    text = file.read()
    shift = int(input("Zadejte posun:"))
    choice = 0
while choice != 1 and choice != 2:
    print("1 - šifrování caesarovou šifrou.")
    print("2 - dešifrování caesarovou šifrou")
    choice = int(input("Zadejte číslo volby:"))
    if choice == 1:
        result = caesar(text, shift)
    if choice == 2:
        result = decaesar(text, shift)
cesta = input("Zadejte cestu k uložení:")
with open(cesta, mode="w", encoding="utf-8") as file:
    file.write(result)

#task e
posun = input("Zadejte posun:")
p = 0
for i in range(len(posun)):
    p += int(posun[i])
if p >= 10:
    posun = str(p)
    p = int(posun[0]) + int(posun[1])
print(p)

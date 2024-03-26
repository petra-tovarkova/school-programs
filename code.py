#task a
def caesar(string, shift):
    result = ""
    for character in string:
        if ord("A") <= character <= ord("a"):
            x = ord(character) + shift
            if x > ord("Z"):
               x -= 26
            result += chr(x)
        else:
            result += character
    return(result)

#task b


#task c
string = input("Zadejte text, který chcete (de)kódovat:")
shift = int(input("Zdejte posun:"))
choice = 0
while choice != 1 and choice != 2:
    print("1 - šifrování caesarovou šifrou.")
    print("2 - dešifrování caesarovou šifrou")
    choice = int(input("Zadejte číslo volby:"))
    if choice == 1:
        result = code(string, shift)
    if choice == 2:
        result = decode(string, shift)
print(result)

#task d


#task e
posun = input("Zadejte posun:")
p = 0
for i in range(len(posun)):
    p += int(posun[i])
if p >= 10:
    posun = str(p)
    p = int(posun[0]) + int(posun[1])
print(p)

#task f
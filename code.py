def code(string, shift):
    result = ""
    for character in string:
        if "A" <= character <= "Z":
            number = ord(character) + shift
            while number > ord("Z"):
                number -= 26
            result += chr(number)
        elif "a" <= character <= "z":
            number = ord(character) + shift
            while number > ord("Z"):
                number -= 26
            result += chr(number)
        else:
            result += character
    return(result)

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
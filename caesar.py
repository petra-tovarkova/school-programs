def caesar(string):
    result = ""
    string = string.upper()
    for character in string:
        if character == " ":
            result += " "
        else:
            number = ord(character) 
            if number > ord("Z"):
                number -= 26
            result += chr(number)
    return result

#Or 
def caesar(string, shift):
    result = ""
    for character in string:
        if character.isalpha():  # Check if the character is alphabetic
            if character.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = (ord(character) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += character
    return result
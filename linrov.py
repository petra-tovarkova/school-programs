import math

a = float(input("Zadej koeficient a: "))
b = float(input("Zadej koeficient b: "))

if a != 0:
    x = -b/a
    print("Lineární rovnice má jeden kořen x =", x)

else:
    print("Nejedná se o lineárni fci")
    

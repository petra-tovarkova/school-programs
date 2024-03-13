import math

a = float(input("zadej koeficient a: "))
b = float(input("zadej koeficient b: "))
c = float(input("zadej koeficient c: "))

if a != 0:
    d = b**2 - 4*a*c

    if d < 0:
        print("Kvadratická rovnice nemá v R řešení. (komplexní kořeny)")

    elif d == 0:
        x = -b / (2*a)
        print("Kvadratická rovnice má jeden kořen x =", x)
        
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Kvadratická rovnice má dva kořeny x1 = ", x1,",x2 = ", x2)

else:
    print("Nejedná se o kvadratickou rovnici!")
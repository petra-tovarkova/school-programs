import math

a = float(input("Zadej stranu a: "))
b = float(input("Zadej stranu b: "))
c = float(input("Zadej stranu c: "))
alfa = float(input("Zadej velikost úhlu alfa ve stupních: "))
beta = float(input("Zadej velikost úhlu beta ve stupních: "))
#třetí úhel je 90 stupňů

if a != 0 and alfa != 0:
    beta = 90 - alfa
    print("beta =", beta)
    c = a/math.sin(math.radians(alfa))
    print("c =", c)
    b = a/math.sin(math.radians(alfa))
    print("b =", b)

elif a != 0 and c != 0:
    b = math.sqrt(c*c - a*a)
    print("b =", b)
    alfa = math.degrees(math.asin(a/c))
    print("alfa =", alfa)
    beta = 90 - alfa
    print("beta =", beta)
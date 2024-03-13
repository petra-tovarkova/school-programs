
a = float(input("Zadej koeficient a: "))
b = float(input("Zadej koeficient b: "))
c = float(input("Zadej koeficient c: "))

if (a+b>c) and (b+c>a) and (a+c>b):
    print("Strany náleží trojúhelníku")

    if (a==b) or (b==c):
        print("Trojúhelník je rovnostranný")

    elif (a==b) or (b==c) or (c==a):
        print("Trojúhelník je rovnoramenný")

    else:
        print("Jedná se o obecný trojúhelník")

else:
    print("Strany nenáleží trojúhelníku")
    

a = float(input("zadej délku strany a: "))
b = float(input("zadej délku strany b: "))

if a == b:
    x = a
    print("Čtverec má délku strany",x,"cm")

elif a < 0:
    print("Není definováno")

elif b < 0:
    print("Není definováno")

else:
    if a > b:
        x = a
        y = b
        print("Obdelník má délky stran",x,"cm x",y,"cm")

    else:
        x = b
        y = a
        print("Obdelník má délky stran",x,"cm x",y,"cm")


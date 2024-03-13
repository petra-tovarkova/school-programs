#Test skupina A, Petra Továrková, 3.A

import random

a = int(input("Zadejte celé číslo z intervalu (5,20) a:"))
b = int(input("Zadejte celé číslo z intervalu (5,20) b:"))
c = random.randint(5,20)
print("Strana c je",c)

if a==b==c:
    print("Strany náleží krychli.")

else:
    print("Strany náleží kvádru.")

if a > b:
    max = a
else:
    max = b
if c > max:
    max = c

print("Největší hrana tělesa je", max,".")

V_krychle = c*c*c
V_telesa = a*b*c

rozdil = (V_krychle) - (V_telesa)
print("Objem krychle o straně c je", V_krychle,"a objem tělesa je",V_telesa,". Rozdíl objemů těles je tedy", rozdil,".")
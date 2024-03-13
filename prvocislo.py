import math

n = int(input("Zadejte přirozené číslo:"))
x = math.floor(math.sqrt(n))

for i in range (2,x +1):
    if n % i == 0:
        print("Číslo",n,"není prvočíslo.")
        break

else:
    if n == 1:
        print("Číslo",n,"není prvočíslo.")
    else:
         print("Číslo",n,"je prvočíslo.")
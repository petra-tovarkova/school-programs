n = int(input("Zadej prostřední hodnotu:"))
k = int(input("Kolik menších a větších čísel se má vypsat?"))

for i in range(n-k,n):
    print(i, end=" ")

print("*",end=" ")

for i in range(n+1,n+k+1):
    print(i, end=" ")    
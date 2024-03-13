#Petra Továrková 3.A, test CYKLY
#Skupina F, Úloha 2


A = int(input("Zadejte první krajní hodnotu intervalu:"))
B = int(input("Zadejte druhou krajní hodnotu intervalu:"))
n = 0
h = 0
 
a = int(input("Zadejte kladné číslo, zda chcete řadu ukončit zadejte 0:"))

while a != 0:
    if (a >= A) and (a <= B):
        n = n + 1
        h = h + a
        a = int(input("Zadejte kladné číslo, zda chcete řadu ukončit zadejte 0:"))

    else:
        a = int(input("Zadejte kladné číslo, zda chcete řadu ukončit zadejte 0:"))

else:
    if n > 0:
             prumer = h/n
             print("V intervalu se nachází",n,"čísel a jejich průměr je",prumer,".")
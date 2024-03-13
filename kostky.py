import random

def hod_kostkou():
    return random.randint(1, 6)

jmeno_A = input("Zadej jméno hráče A: ")
jmeno_B = input("Zadej jméno hráče B: ")
jmeno_C = input("Zadej jméno hráče C: ")

hod_A = hod_kostkou()
hod_B = hod_kostkou()
hod_C = hod_kostkou()

print("{}: {}".format(jmeno_A, hod_A))
print("{}: {}".format(jmeno_B, hod_B))
print("{}: {}".format(jmeno_C, hod_C))

if hod_A > hod_B and hod_A > hod_C:
    print("Vítěz: {}".format(jmeno_A))
elif hod_B > hod_A and hod_B > hod_C:
    print("Vítěz: {}".format(jmeno_B))
elif hod_C > hod_A and hod_C > hod_B:
    print("Vítěz: {}".format(jmeno_C))
else:
    max_hod = max(hod_A, hod_B, hod_C)
    vitezi = [jmeno for jmeno, hod in zip([jmeno_A, jmeno_B, jmeno_C], [hod_A, hod_B, hod_C]) if hod == max_hod]
    print("Vítězové: {} s hodem {}".format(', '.join(vitezi), max_hod))

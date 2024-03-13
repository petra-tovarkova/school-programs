import random

# Simulace hodu kostkou pro jednoho hráče
def hod_kostkou():
    return random.randint(1, 6)

# Zadání jmen hráčů
jmeno_A = input("Zadej jméno hráče A: ")
jmeno_B = input("Zadej jméno hráče B: ")
jmeno_C = input("Zadej jméno hráče C: ")

# Seznam hráčů
hraci = [jmeno_A, jmeno_B, jmeno_C]

# Seznam pro ukládání hodů jednotlivých hráčů
hody = {}

# Simulace hodu kostkou pro každého hráče
for hrac in hraci:
    hody[hrac] = hod_kostkou()

# Vypsání hodů jednotlivých hráčů
for hrac, hod in hody.items():
    print(f'{hrac}: {hod}')

# Určení vítěze nebo vítězů
max_hod = max(hody.values())
vitezi = [hrac for hrac, hod in hody.items() if hod == max_hod]

# Vypsání vítěze nebo vítězů s jejich jménem
if len(vitezi) == 1:
    print(f'Vítěz: Hráč {vitezi[0]}')
else:
    print(f'Vítězové: Hráči {", ".join(vitezi)}')

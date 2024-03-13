def nejvetsi(a,b,c):
    if a > b:
        max = a
    else:
        max = b
    if c > max:
        max = c
    print("Největší číslo je", max)
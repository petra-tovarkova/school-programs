import math

a = float(input("Zadejte plnou cenu vstupenky:"))

sleva = 0.65*a

sleva = math.ceil(sleva)
print("Cena plné vstupenky po zaokrouhlení je",sleva)
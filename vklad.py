vklad = int(input("Zadej vklad: "))
print(vklad, "kč")
mira = int(input("Zadej roční úrokovou míru: "))
mira = mira*0.01
(print("Zůstatek na účtě:",vklad*mira))
zustatek = vklad*mira
print("Daň z připsaných úroků je 15%")
print("Zůstatek na účtě:",0.15*zustatek)


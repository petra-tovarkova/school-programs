class Člověk:
    def __init__(self, jmeno, vek, vyska, vaha):
        self.jmeno = jmeno
        self.vek = vek
        self.vyska = vyska
        self.vaha = vaha

    def povolani(self):
        print("Jsem", self.povolani)

    def __str__(self):
        return "Jmenuji se" + self.name + "a je mi" + self.vek, "let." + "Měřím" + self.vyska + "cm a vážím" + self.vaha

class Dítě(Člověk):
    def init(self, skola):
        super().__init__(jmeno, vek, vyska, vaha)
#    jmeno = input("Zadej jméno:")
#    vek = input("Zadej věk:")
#    vyska = input("Zadej kolik měříš:")
#    vaha = input("Zadej kolik vážíš:")
#    skola = input("Zadej školu na kterou chodíš:")

    def __str__(self):
        return 



class Teenager(Člověk):



class Dospělí(Člověk):





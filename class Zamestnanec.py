class Zamestnanec:
    def __init__(self, jmeno, pozice, dovolena):
        self.jmeno = jmeno
        self.pozice = pozice
        self.dovolena = 25

    def cerpani_dovolene(self, dny):
        if self.dovolena < dny:
            return "Máte nárok na" + str(self.dovolena) + "dní."
        else:
            self.dovolena -= dny
            return "Dovolená byla udělena, zbývá ještě" + str(self.dovolena) + "dní."
        
    def __str__(self):
        return self.jmeno + "pracuje na pozici" + self.pozice + "."
    
class Manažer(Zamestnanec):
    def __init__(self, jmeno, pozice, pocet_podrizenych):
        super().__init__(jmeno, pozice)
        self.pocet_podrizenych = pocet_podrizenych

    def __str__(self):
        return super().__str__() + "a má" + str(self.pocet_podrizenych) + "podřízených."

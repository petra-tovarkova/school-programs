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
    def __init__(self, jmeno, pozice, pocet_podrizenych, dovolena):
        super().__init__(jmeno, pozice, dovolena)
        self.pocet_podrizenych = pocet_podrizenych

        self.podrizeni = []
    
    def pridej_podrizeneho(self, podrizeny):
        self.podrizeni.append(podrizeny)

    def vypis_podrizenych(self):
        for i in range(self.podrizeni):
            print(i.jmeno)

    def __str__(self):
        return super().__str__() + "Má" + len(self.podrizeni) + "podřízených."
    
class Zam_castecny(Zamestnanec):
    def __init__(self, jmeno, pozice, dovolena, uvazek):
        super().__init__(jmeno, pozice, dovolena)
        self.uvazek = uvazek

    def __str__(self):
        return self.jmeno + "Pracuje na pozici" + self.pozice + "s úvazkem" + self.uvazek + "."
    

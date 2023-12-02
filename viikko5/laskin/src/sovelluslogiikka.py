class Sovelluslogiikka:
    def __init__(self, tulos=0, edellinen=0):
        self.tulos = tulos
        self.edellinen = edellinen

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo


class Summa:
    def __init__(self, sovelluslogiikka, lue_syote) -> None:
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
            if len(luku) == 0:
                return
        except Exception:
            pass
        
        tulos = self.sovelluslogiikka.tulos + int(luku)
        self.sovelluslogiikka.aseta_arvo(tulos)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote) -> None:
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            luku = self.lue_syote()
            if len(luku) == 0:
                return
        except Exception:
            pass

        tulos = self.sovelluslogiikka.tulos - int(luku)
        self.sovelluslogiikka.aseta_arvo(tulos)

class Nollaus:
    def __init__(self, sovelluslogiikka) -> None:
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka) -> None:
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.edellinen)
        self.sovelluslogiikka.edellinen = tulos
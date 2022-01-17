class Kunde:
    def __init__(self,vorname, nachname, alter, geschlecht, adresse, konto):
        self.vorname=vorname
        self.nachname=nachname
        self.alter=alter
        self.geschlecht=geschlecht
        self.adresse=adresse
        self.konto=konto
        print("Objekt ", self, " wird erzeugt.")
    def __del__(self):
        print("Objekt ", self, " wird beseitigt.")

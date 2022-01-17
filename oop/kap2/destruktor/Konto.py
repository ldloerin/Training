class Konto:
    def __del__(self):
        print("Objekt ", self, " wird beseitigt.")
 
    def __init__(self,kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp
        print("Objekt ", self, " wird erzeugt.")
        
    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag
    def auszahlen(self, betrag):
        pass

from Konto import *
class Programm:
    def einzahlen(self,betrag):
        self.kontostand += betrag
    def main():
        konto = Konto(1000,"Girokonto")
        print("Das Dictionary __dict__:", konto.__dict__)
        konto.eigentuemer = "Ralph"
        print("Das Dictionary __dict__:", konto.__dict__)
        konto.einzahlen = Programm.einzahlen
        print("Das Dictionary __dict__:", konto.__dict__)
        konto.einzahlen(konto, 123)
        print(konto.kontostand)
        konto.getTyp = lambda: konto.kontotyp
        print("Das Dictionary __dict__:", konto.__dict__)
        print(konto.getTyp())
        
       
    def __init__(self):
        Programm.main()
Programm()




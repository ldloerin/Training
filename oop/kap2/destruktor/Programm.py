from Kunde import *
from Konto import *
class Programm:
    def main():
        konto1 = Konto(1000,"Girokonto")
        kunde1 = Kunde("Hans","Dampf",42,"Mann","Milchstrasse 123, 666 Irgendwo", konto1)
        del konto1
        print("-" * 30)
        print("Kontostand bei Beginn:\t", kunde1.konto.kontostand)
        kunde1.konto.einzahlen(123)
        print("Neuer Kontostand:\t", kunde1.konto.kontostand)

    def __init__(self):
        Programm.main()
Programm()




from Kunde import *
from Konto import *


class Programm:
    def __init__(self):
        Programm.main()

    def main():
        konto1 = Konto(1000)
        kunde1 = Kunde("Hans","Dampf",42,"Mann","Milchstrasse 123, 666 Irgendwo", konto1)
        print("Kontostand bei Beginn:\t", kunde1.konto.getKontostand())
        kunde1.konto.einzahlen(123)
        print("Kontostand bei Beginn:\t", kunde1.konto.getKontostand())
        # kunde1.konto.kontostand = -5
        # print("Neuer Kontostand:\t", kunde1.konto.kontostand)


Programm()

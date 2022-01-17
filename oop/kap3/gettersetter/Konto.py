class Konto:
    def __init__(self,kontostand):
        self.__kontostand = kontostand

    def einzahlen(self, betrag):
        self.__kontostand = self.__kontostand + betrag

    def auszahlen(self, betrag):
        self.__kontostand = self.__kontostand + betrag

    def getKontostand(self):
        return self.__kontostand
    
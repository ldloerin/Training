from Konto import *
class Programm:
    def main():
        konto = Konto(1000,"Girokonto")
        print(konto.kontostand)
        print(konto.eigentuemer)
        print(konto.eigentuemer.name)
       
    def __init__(self):
        Programm.main()
Programm()




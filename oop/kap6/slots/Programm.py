from Konto import *
class Programm:
    def main():
        konto = Konto(1000,"Girokonto")
        
        print("__slots__:", konto.__slots__)
    def __init__(self):
        Programm.main()
Programm()




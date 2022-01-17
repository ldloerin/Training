from Konto import *
class Programm:
    def main():
        konto = Konto(1000,"Girokonto")
        print(type(konto))
        print(type(5))
        Tier=type("Tier",(),{"alter":3})
        tier = Tier()
        print(type(tier))
        

       
    def __init__(self):
        Programm.main()
Programm()




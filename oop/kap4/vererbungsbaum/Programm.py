from Katze import *
from Hund import *
from Vogel import *

class Programm:
    def main():
        katze = Katze(1,"Susi")
        vogel = Vogel(3)
        hund = Hund(2)
        hund.bellen()
        katze.miauen()
        print(vogel.alter)


    def __init__(self):
        Programm.main()
Programm()




from Katze import *
from Hund import *
class Programm:
    def main():
        katze = Katze(1)
        katze.lautgeben()
        hund = Hund(3)
        hund.lautgeben("Miau")
    


    def __init__(self):
        Programm.main()
Programm()




from Ausnahme import *
from MeineAusnahme import *
class Programm:
    def main():
        obj = Ausnahme()
        try:
            obj.verifiziere()
        except MeineAusnahme:
            print("Es gab Porbleme")
    def __init__(self):
        Programm.main()
Programm()




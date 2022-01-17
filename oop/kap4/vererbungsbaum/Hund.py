from Saeugetier import *
class Hund(Saeugetier):
    def __init__(self,alter):
        Tier.__init__(self,alter)
    def bellen(self):
        print("Wau")

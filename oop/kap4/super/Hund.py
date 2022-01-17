from Tier import *
class Hund(Tier):
    def __init__(self,alter):
        Tier.__init__(self,alter)

    def lautgeben(self):
        print("Wau, wau, wuff")

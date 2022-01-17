from Tier import *
class Katze(Tier):
    def __init__(self,alter):
        Tier.__init__(self,alter)

    def lautgeben(self):
        print("Mau, mau, miiiau")

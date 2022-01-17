from Katze import *


class Programm:
    def __init__(self):
        self.main()

    def main(self):
        susi = Katze(1)
        print(susi.alter)
        susi.alter = 2
        print(susi.alter)


Programm()

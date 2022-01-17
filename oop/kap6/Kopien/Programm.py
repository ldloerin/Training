from Tier import *
class Programm:
    def main():
        t1 = Tier(2)
        print(t1.alter)
        t2 = t1
        t2.alter = 3
        print(t1.alter)
       
    def __init__(self):
        Programm.main()
Programm()




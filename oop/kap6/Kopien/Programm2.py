from Tier import *
from copy import *
class Programm2:
    def main():
        t1 = Tier(2)
        print(t1.alter)
        t2 = copy(t1)
        t3 = deepcopy(t1)

        t2.alter = 3
        print(t1.alter)
        t3.alter = 4
        print(t1.alter)
       
    def __init__(self):
        Programm2.main()
Programm2()




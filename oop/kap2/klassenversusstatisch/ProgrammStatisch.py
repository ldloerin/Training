from Rechne import *
class ProgrammStatisch:
    def main():
        Rechne.multipliziere(22,20)
        obj = Rechne()
        print(obj.addiere(33,30))
        obj.rechne()


    def __init__(self):
        ProgrammStatisch.main()
ProgrammStatisch()

class Rechne:
    @staticmethod    
    def addiere(a,b):
        return a + b
    @staticmethod
    def multipliziere(a,b):
        return a * b
    @staticmethod
    def dividiere(a,b):
        return a / b
    @staticmethod
    def punktrechnung():
        print(Rechne.multipliziere(21,2))
        print(Rechne.dividiere(21,2))
        obj = Rechne()
        print(obj.addiere(5, 6))
    
    @classmethod 
    def rechne(cls):
        print(cls.addiere(22,20))
        print(Rechne.multipliziere(22,20))
        cls.punktrechnung()
        obj = Rechne()
        print(obj.addiere(15, 6))
        




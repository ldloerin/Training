class KlasseVersusInstanz:
    klassenvariable = 42
    def __init__(self):
        self.instanzvariable=True
        
    def instanzmethode1(self, parameter):
        print(self.instanzvariable)
        print(parameter)
        print(KlasseVersusInstanz.klassenvariable)
    def instanzmethode2(self):
        print(self.instanzvariable)
        
    def methodeklasse():
        print("Methode der Klasse")
        print(KlasseVersusInstanz.klassenvariable)
       

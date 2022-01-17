from Tier import *
from Eigentuemer import *
class Katze(Tier,Eigentuemer):
    def __init__(self,alter,name, wohnort, person):
        Tier.__init__(self,alter)
        Eigentuemer.__init__(self,wohnort, person)
        self.__name = name
        
    def __getName(self):
        return self.__name

    name = property(__getName)

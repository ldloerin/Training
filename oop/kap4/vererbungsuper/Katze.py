from Tier import *
class Katze(Tier):
    def __init__(self,alter,name):
        super().__init__(alter)
        self.__name = name
        
    def __getName(self):
        return self.__name

    name = property(__getName)

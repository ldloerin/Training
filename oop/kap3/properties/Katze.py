class Katze:
    def __init__(self, alter):
        self.__alter = alter

    def __set_alter(self, alter):
        self.__alter = alter

    def __get_alter(self):
        return self.__alter
    
    alter = property(__get_alter, __set_alter)

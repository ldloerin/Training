import math


class Pizza():
    def __init__(self, diameter):
        self.radius = diameter / 2

    @classmethod
    def margharita(cls):
        cls.margharita_covering = ['mozzarella', 'tomato']
        print(cls.margharita_covering)

    @classmethod
    def prosciutto(cls):
        cls.prosciutto_covering = ['mozzarella', 'tomato', 'ham']
        print(cls.prosciutto_covering)

    def area(self):
        print('Pizza area:', self.circle_area(self.radius))

    @staticmethod
    def circle_area(r):
        return math.pi * r ** 2


Pizza.margharita()
Pizza.prosciutto()
my_pizza = Pizza(20)
my_pizza.area()

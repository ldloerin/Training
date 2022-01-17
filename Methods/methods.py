import math


class Pizza:
    def __init__(self, diameter):
        self.radius = diameter / 2

    @classmethod
    def margharita(cls):
        cls.margharita_covering = ['mozzarella', 'tomato']
        cls.margharita_price = 5
        return cls.margharita_covering

    @classmethod
    def prosciutto(cls):
        cls.prosciutto_covering = ['mozzarella', 'tomato', 'ham']
        cls.prosciutto_price = 6
        return cls.prosciutto_covering

    @classmethod
    def overview(cls):
        cls.margharita()
        cls.prosciutto()
        print('Margharita:', str(cls.margharita_price), '€ --- Ingredients:', cls.margharita_covering)
        print('Prosciutto:', str(cls.prosciutto_price), '€ --- Ingredients:', cls.prosciutto_covering)

    def area(self):
        print('Pizza area:', self.circle_area(self.radius))
        print(dir(self.prosciutto))

    @staticmethod
    def circle_area(r):
        return math.pi * r ** 2


#print(Pizza.margharita())
#Pizza.overview()
my_pizza = Pizza(20)
my_pizza.area()

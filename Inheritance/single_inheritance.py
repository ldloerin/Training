class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound="nothing"):
        print(self.name, "barks", sound)


class LabradorOrigin:
    origin = "UK"


class Labrador(Dog, LabradorOrigin):
    def speak(self, sound="wau"):
        print(self.name, "says", sound)


class Dachshund(Dog):
    def speak(self, sound="wau wau"):
        print(self.name, "says", sound)


class Terrier(Dog):
    def speak(self, sound="wuff"):
        print(self.name, "says", sound)
        return super().speak(sound)


bob = Labrador("Bob", 1.5)
tom = Dachshund("Tom", 4)
tim = Terrier("Tim", 4)
tim.speak('grrrr')
tim.speak()
print(bob.origin)

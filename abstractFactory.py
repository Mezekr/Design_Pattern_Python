
class Dog:
    """ One of the objects to be returned"""

    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"


class DogFactory:
    """ Create a factory"""

    def get_pet(self, name):
        """ Returna a Dog object"""
        return Dog()

    def get_food(self):
        """ Return a Dog Food object"""
        return "Dog Food!"

    

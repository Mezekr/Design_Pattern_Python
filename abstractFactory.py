
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

class PetStore:
    """ PetStore houses the ability Factory"""
    
    def __init__(self, pet_factory:None):
        """ pet_factory is the Abstract Factory"""
        self._pet_factory = pet_factory
    
    def show_pet(self,):
        """ Utility method to display the details of the object"""
        
        # Create the objects from the concrete Factory
        pet = self._pet_factory.get_pet("My Dog")
        pet_food = self._pet_factory.get_food()
        
        print(f"Our pet is {pet}!")
        print(f"Our pet says hello by calling { pet.speak()} ")
        print(f"Its Food is {pet_food}")
        

# Create a concrete Factory
factory = DogFactory()

# Create a pet store housing our abstract factory
shop = PetStore(factory)

# Invoke the utility method to shaow the details of our pet
shop.show_pet()


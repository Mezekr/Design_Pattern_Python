class Dog:
    """ A simple dog class"""

    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:
    """ A simple cat class"""

    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Meaw!"

def get_pet(pet="dog"):
    """The Factory method
    Args:
        pet (str, optional): _description_. Defaults to "dog".
    """

    pets = dict(dog= Dog("Hope"), cat= Cat("Peace"),)
    return pets[pet]


my_dog = get_pet("dog")
print(my_dog.speak())

my_cat = get_pet("cat")
print(my_cat.speak())
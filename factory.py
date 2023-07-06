class Dog:
    """ A simple dog class"""

    def __init__(self,name):
        self.name = name

    def speak():
        return "Woof!"

def get_pet(pet="dog"):
    """The Factory method
    Args:
        pet (str, optional): _description_. Defaults to "dog".
    """

    pets = dict(dog= Dog("Hope"))
    return pets[pet]

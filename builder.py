# Product: The object tobe created
class Car:
    """Product: The object to be created"""
    def __init__(self):
        self.name = None
        self.model = None
        self.tires = None
        self.engine = None
    def __str__(self):
        return f'{self.name} | {self.model} | {self.tires}'

class Builder:
    """ abstract Builder (Interface) """

    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()

class MazdaBuilder(Builder):
    """ Concrete Car builder"""
    def add_name(self):
        self.car.name = "Mazda"
    
    def add_model(self):
        self.car.model = "MX-30"

    def add_tires(self):
        self.car.tires = "Regular tires"
    
    def add_engine(self):
        self.car.engine = "Turbo Engine"
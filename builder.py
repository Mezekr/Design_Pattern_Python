# Product: The object tobe created
class Car:
    def __init__(self):
        self.name = None
        self.model = None
        self.tires = None
        self.engine = None
    def __str__(self):
        return f'{self.name} | {self.model} | {self.tires}'
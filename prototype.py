# Prototype designe pattern example

import copy

class Prototype:
    """Prototype designe pattern class"""

    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        """ Registers an object """
        self.self._objects[name] = obj

    def unregister(self, name):
        """ Unregisters an object """
        del self._objects[name] 

    def clone(self, name, **attr):
        """Clones a registered object and updates its attributes"""
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(attr)   
        return cloned_obj

class Car:
    """ Object to be cloned. """
    
    def __init__(self):
        self.name = "Skylark"
        self.color = "Black"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name}| ({self.color}| {self.options}."


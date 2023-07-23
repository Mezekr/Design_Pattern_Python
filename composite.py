# Composite desgin pattern example

class Component:
    """Abstract class"""

    def __init__(self,*args, **kwargs):
        pass
    def component_functions(self):
        pass

# Inherits from Composite anbstract class
class Child(Component):
    """Concrete class"""

    def __init__(self,*args, **kwargs):
        Component.__init__(self, *args, **kwargs)

    # This is where the the Name of the Child item stores!
    self.name = args[0]

    # define the abstract method component_function of the parent abstract  class
    def component_function(self):
        # prints Name of the Child item
        print(f"{self.name}")

# Create a class that inherits from the abstract class, Component
class Composite(Component):
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

    # This is where the the Name of the composite object stores
    self.name = args[0]

    # List, where the the Child item keeps 
    self.children = []

    def child_append(self, child):
        """ Method to add a new child item"""
        self.child_append(child)
    def child_remove(self, child):
        """ Method to remove a child"""
        self.children.remove(child)

    def component_functions(self):
        # Print the name of the composite object
        print(f"{self.name}")

        # Iterate through the child objects and invoke the component functions
        for child in self.children:
            child.component_function()
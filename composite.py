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

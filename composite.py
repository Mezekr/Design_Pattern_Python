# Composite desgin pattern example

class Component:
    """Abstract class"""

    def __init__(self,*args, **kwargs):
        pass
    def component_function(self):
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

    def append_child(self, child):
        """ Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """ Method to remove a child"""
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print(f"{self.name}")

        # Iterate through the child objects and invoke the component functions
        for child in self.children:
            child.component_function()

# Build a composite submenu 1
sub_1 = Composite("submenu 1")

# Create a new child sub_submenu 11
sub_11 = Child("sub_submenu 11")

# Create a new child sub_submenu 12 
sub_12 = Child("sub_submenu 12")

# Add the sub_submenu 11 to submenu 1
sub_1.append_child(sub_11)

# Add the sub_submenu 12 to submenu 1
sub_1.append_child(sub_12)

# Build the top level composite menu
top_menu = Composite("top menu")

# Build a submenu 2 that is not composite 
sub_2 = Child("sub_submenu 2")

# Add the composite submenu 1 to the top-level composite menu
top_menu.append_child(sub_1)

# Add the plain submenu 2 to the top-level composite menu
top_menu.append_child(sub_2)

# Let's test if our composite parent works properly
top_menu.component_function()
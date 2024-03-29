# Adapter desgine pattern example 

class Eritrean:
    """ Tigrinya speaker"""

    def __init__(self):
        self.name = "Tigrinya"

    def speak_tigrinya(self):   
        return "Selam, Alem!" # means Hello World

class British:
    """English speaker""" 	
    def __init__(self):
        self.name = "English"

    def speak_English(self):
        return "Hello, World!"

class Adapter:
    """Changes the generic method name to individual method name"""

    def __init__(self, object, **adapter_method):
        """Changes the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between the methods
        # For example, speak() will be translated to speak_tigrinya() 
        self.__dict__.update(adapter_method)

    def __getattr__(self, attr):
        """Returns the rest of the attributes!"""
        return getattr(self._object, attr)
    
# List to store the speaker objects
objects = list()

# Create a Eritrean speaker object
eritrean = Eritrean()   

# Create a British speaker object
british = British()

# Append the speaker object to the speaker objectws list
objects.append(Adapter(eritrean, speak=eritrean.speak_tigrinya))
objects.append(Adapter(british, speak=british.speak_English))

# test the adapter design pattern 

for object in objects:
    print(f'{object.name} says, "{object.speak()}"')

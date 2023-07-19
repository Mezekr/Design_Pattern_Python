# Adapter desgine pattern example 

class Eritrean:
    """ Tigrinya speaker"""

    def __init__(self):
        self.name = "Tigrinya"

    def speak_tigrinya(self):   
        return "Selem, Alem!" # means Hello World

class British:
    """English speaker""" 	
    def __init__(self):
        self.name = "English"

    def speak_English(self):
        return "Hello, World!"
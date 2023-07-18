# Decorator desgine pattern example 
from functools import wraps

def make_blink(function):
    """Defines a decorator"""

    # This makes the decorated transparent in terms of its name and docs


    # Defines the inner function

    def decorator():
        # Grab the return value of the function being decorated


        # add new functionality to the function being decorated

        return decorator
    

# Defines the inner function
def hello_world():
    """ Original function"""
    return "Helo, World!"
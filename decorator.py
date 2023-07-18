# Decorator desgine pattern example 
from functools import wraps

def make_blink(function):
    """Defines a decorator"""

    # This makes the decorated transparent in terms of its name and docs
    @wraps(function)

    # Defines the inner function
    def decorator():
        # Grab the return value of the function being decorated
        fun_return = function()

        # add new functionality to the function being decorated
        return "<blink>" + fun_return + "</blink>"

    return decorator
    

# Defines the inner function and apply the decorated function
@make_blink
def hello_world():
    """ Original function"""
    return "Helo, World!"

class Borg:
    """The Borg design pattern in python."""

    _shared_data = {} # Class attribute dictionary

    def __init__(self):
        # Make the class attribute dictionary to instant attribute
        self.__dict__ = self._shared_data

class Singleton(Borg):
    """ Class to implement singleton design pattern."""

    def __init__(self, **kwargs):
        Borg.__init__(self)

        # update the attributes dictionary by inserting key-value pairs
        Borg._shared_data.update(kwargs)

        # Returns the string representation of of the object
    def __str__(self):
        return str(self._shared_data)

# Let's create the first singleton instance and add first acronym
HTTP_singleton_instance = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(HTTP_singleton_instance)

#Let's create the second object and add second acronym
# see if refers to the the same attribute dictionary

SNMP_singleton_instance = Singleton(SNMP = "Simple Network Management Protocol")

print(SNMP_singleton_instance)

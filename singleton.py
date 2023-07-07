
class Borg:
    """The Borg design pattern in python."""

    _shared_data = {} # Class attribute dictionary

    def __init__(self):
        # Make the class attribute dictionary to instant attribute
        self.__dict__ = self._shared_data


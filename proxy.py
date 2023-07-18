# Proxy desgin pattern example

import time

class Producer:
    """Defines the 'Resource intensive' object to instantiate"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time for meeting!")
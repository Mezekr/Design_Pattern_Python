# Proxy desgin pattern example

import time

class Producer:
    """Defines the 'Resource intensive' object to instantiate"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Defines the ' Relatively less resource intensive' proxy to instantiate"""
    
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if the Producer is available"""
        print("Artist checking if the Producer is available... ")

        time_to_wait = 2
        if self.occupied == 'No':
            # If the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(time_to_wait)

            # Make the producer meet the guest
            self.producer.meet()
        else:
            # Otherwise, do not instaniate a producer
            time.sleep(time_to_wait)
            print("Producer is busy!")

# Instantiatre a Proxy
proxy = Proxy()

# Make the Proxy: Artist produce as long as Producer is available
proxy.produce()

# change the state to 'occupied'
proxy.occupied = 'Yes'

# Make the Producer produce
proxy.produce()

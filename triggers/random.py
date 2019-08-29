"""Random trigger class. Will randomly trigger and stop an alert."""

import random
from .trigger import Trigger


class RandomTrigger(Trigger):

    def tick(self):
        if random.randint(0, 10) > 5:
            self.broker.trigger(self.alert)
        else:
            self.broker.stop(self.alert)

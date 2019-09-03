"""Handler using the ThingM blink(1)."""

import logging
import time
from .handler import Handler
from blink1.blink1 import Blink1, Blink1ConnectionFailed


class BlinkHandler(Handler):

    def __init__(self, *args, **kwargs):
        self.color = '#ffffff'
        if 'color' in kwargs:
            self.color = kwargs.pop('color')
        super(BlinkHandler, self).__init__(*args, **kwargs)

    def blink(self):
        try:
            blink1 = Blink1()
        except Blink1ConnectionFailed as e:
            logging.error('Blink1 error: %s', e)
            return
        blink1.fade_to_color(300, self.color)
        time.sleep(0.3)
        blink1.fade_to_color(300, '#000000')
        blink1.close()

    def alert_on(self):
        self.blink()

    def alert_ongoing(self):
        self.blink()

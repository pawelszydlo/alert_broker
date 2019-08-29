"""Dummy handler class. Will print the alerts."""

from .handler import Handler


class DummyHandler(Handler):
    def alert_on(self):
        print('%s poped!' % self.alert)

    def alert_off(self):
        print('%s disappeared!' % self.alert)

    def alert_ongoing(self):
        print('%s ongoing!' % self.alert)

"""Handler class. All handlers must inherit from it."""


class Handler:
    def __init__(self, alert: str, interval=2):
        self.broker = None
        self.interval = interval
        self.alert = alert

    def alert_on(self):
        """Will be run when alert pops up."""
        pass

    def alert_off(self):
        """Will be run when alert disappears."""
        pass

    def alert_ongoing(self):
        """Will be run every second when the alert is up."""
        pass

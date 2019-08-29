"""Trigger class. All triggers must inherit from it."""
import asyncio


class Trigger:
    """Base class for triggers."""

    def __init__(self, alert: str, interval: int = 2):
        self.broker = None
        self.interval = interval
        self.alert = alert

    def tick(self):
        """Will be run periodically, every interval."""
        raise NotImplementedError('You must implement this.')

    async def start(self):
        """Will be run by the broker. Better not override this."""
        while True:
            self.tick()
            await asyncio.sleep(self.interval)

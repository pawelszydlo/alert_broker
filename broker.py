"""Alerts broker - main class."""

import asyncio
import logging
import sys
from collections import defaultdict

from handlers.handler import Handler
from triggers.trigger import Trigger

assert sys.version_info >= (3, 7), 'Script requires Python 3.7+.'
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.DEBUG)


class Broker:
    def __init__(self):
        self._active_alerts = set()
        self._triggers = []
        self._handlers = defaultdict(list)

    @property
    def active_alerts(self):
        return self._active_alerts

    def register_trigger(self, trigger: Trigger):
        """Register a new trigger."""
        trigger.broker = self
        self._triggers.append(trigger)

    def register_handler(self, handler: Handler):
        """Register a new handler."""
        handler.broker = self
        self._handlers[handler.alert].append(handler)

    def trigger(self, alert: int):
        """Trigger alert."""
        LOGGER.info('Triggering: %s', alert)
        self._active_alerts.add(alert)

    def stop(self, alert: int):
        """Stop an alert."""
        LOGGER.info('Stopping: %s', alert)
        self._active_alerts -= {alert}

    async def alert_monitor(self):
        """Start the alert monitor loop."""
        last_alerts = set()
        while True:
            # New alerts.
            new_alerts = self.active_alerts - last_alerts
            for alert in new_alerts:
                for handler in self._handlers.get(alert, []):
                    handler.alert_on()
            # Gone alerts.
            for alert in last_alerts - self.active_alerts:
                for handler in self._handlers.get(alert, []):
                    handler.alert_off()
            # Ongoing alerts.
            for alert in self.active_alerts - new_alerts:
                for handler in self._handlers.get(alert, []):
                    handler.alert_ongoing()
            last_alerts = self.active_alerts.copy()
            await asyncio.sleep(1)

    async def start_tasks(self):
        """Starts all the tasks asynchronously."""
        tasks = []
        # Add all the triggers.
        for trigger in self._triggers:
            tasks.append(trigger.start())
        # Add the alert monitor.
        tasks.append(self.alert_monitor())
        # Await for all the tasks to finish.
        await asyncio.gather(*tasks)

    def run(self):
        """Run the event loop."""
        LOGGER.info('Starting main loop...')
        asyncio.run(self.start_tasks())

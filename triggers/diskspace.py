"""Will trigger an alert if the disk space falls below specified min value."""

import logging
import shutil
from .trigger import Trigger


class DiskSpaceTrigger(Trigger):

    def __init__(self, alert, path: str, min_free_mb: int, interval=60):
        super(DiskSpaceTrigger, self).__init__(alert, interval)
        self.path = path
        self.min_free = min_free_mb * 2 ** 20

    def tick(self):
        _, _, free = shutil.disk_usage(self.path)
        logging.info(
            'Free space on "%s": %.2f GB, threshold: %.2f GB',
            self.path, free / 2 ** 30, self.min_free / 2 ** 30)
        if free < self.min_free:
            self.broker.trigger(self.alert)
        else:
            self.broker.stop(self.alert)

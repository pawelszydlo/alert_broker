"""Will trigger an alert if the disk space falls below specified min value."""

import logging
import shutil
from .trigger import Trigger


class DiskSpaceTrigger(Trigger):

    def __init__(self, *args, **kwargs):
        self.path = kwargs.pop('path')  # type: str
        self.min_free = kwargs.pop('min_free_mb') * 2**20
        super(DiskSpaceTrigger, self).__init__(*args, **kwargs)

    def tick(self):
        _, _, free = shutil.disk_usage(self.path)
        logging.info(
            'Free space on "%s": %.2f GB, threshold: %.2f GB',
            self.path, free / 2**30, self.min_free / 2**30)
        if free < self.min_free:
            self.broker.trigger(self.alert)
        else:
            self.broker.stop(self.alert)

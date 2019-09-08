"""Handler to execute a command on alert."""

import logging
import subprocess
from .handler import Handler


class CommandHandler(Handler):

    def __init__(self, *args, **kwargs):
        self.command_on = kwargs.pop('command_on', None)
        self.command_off = kwargs.pop('command_off', None)
        self.command_ongoing = kwargs.pop('command_ongoing', None)
        super(CommandHandler, self).__init__(*args, **kwargs)

    def alert_on(self):
        if self.command_on:
            logging.info('Running: %s', self.command_on)
            process = subprocess.Popen(self.command_on.split())
            process.communicate()

    def alert_off(self):
        if self.command_off:
            logging.info('Running: %s', self.command_off)
            process = subprocess.Popen(self.command_off.split())
            process.communicate()

    def alert_ongoing(self):
        if self.command_ongoing:
            logging.info('Running: %s', self.command_ongoing)
            process = subprocess.Popen(self.command_ongoing.split())
            process.communicate()

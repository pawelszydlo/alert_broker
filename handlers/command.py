"""Handler to execute a command on alert."""

import logging
import subprocess
from .handler import Handler


class CommandHandler(Handler):

    def __init__(self, alert, command_on: str = None, command_off: str = None,
                 command_ongoing: str = None):
        super(CommandHandler, self).__init__(alert)
        self.command_on = command_on
        self.command_off = command_off
        self.command_ongoing = command_ongoing

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

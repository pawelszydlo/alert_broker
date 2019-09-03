"""Will trigger an alert if the provided system command will return an error."""

import logging
import subprocess
from .trigger import Trigger


class CommandTrigger(Trigger):

    def __init__(self, *args, **kwargs):
        self.command = None
        if 'command' in kwargs:
            self.command = kwargs.pop('command')
        super(CommandTrigger, self).__init__(*args, **kwargs)

    def tick(self):
        if not self.command:
            logging.error('You must provide a command to run.')
            return
        process = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE)
        process.communicate()
        if process.returncode:
            logging.info(
                'Command "%s" had non-zero exit status.', self.command)
            self.broker.trigger(self.alert)
        else:
            self.broker.stop(self.alert)

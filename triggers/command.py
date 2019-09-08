"""Will trigger an alert if the provided system command will return an error."""

import logging
import subprocess
from .trigger import Trigger


class CommandTrigger(Trigger):

    def __init__(self, *args, **kwargs):
        self.command = kwargs.pop('command')  # type: str
        super(CommandTrigger, self).__init__(*args, **kwargs)

    def tick(self):
        process = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE)
        process.communicate()
        if process.returncode:
            logging.info(
                'Command "%s" had non-zero exit status.', self.command)
            self.broker.trigger(self.alert)
        else:
            self.broker.stop(self.alert)

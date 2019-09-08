"""Will trigger an alert if the provided system command will return an error."""

import logging
import re
import subprocess
from .trigger import Trigger


class CommandTrigger(Trigger):

    def __init__(self, *args, **kwargs):
        self.command = kwargs.pop('command')  # type: str
        if 'regexp' in kwargs:
            self.regexp = re.compile(kwargs.pop('regexp'))
        else:
            self.regexp = None
        if 'negative_regexp' in kwargs:
            self.negative_regexp = re.compile(kwargs.pop('negative_regexp'))
        else:
            self.negative_regexp = None
        super(CommandTrigger, self).__init__(*args, **kwargs)

    def tick(self):
        process = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE)
        output, _ = process.communicate()
        if process.returncode:
            logging.info(
                'Command "%s" had non-zero exit status.', self.command)
            self.broker.trigger(self.alert)
        elif self.regexp and self.regexp.match(str(output)):
            logging.info(
                'Regexp match on output from command "%s".', self.command)
            self.broker.trigger(self.alert)
        elif self.negative_regexp and not self.negative_regexp.match(
                str(output)):
            logging.info(
                'Regexp not matched on output from command "%s".', self.command)
            self.broker.trigger(self.alert)
        else:
            self.broker.stop(self.alert)

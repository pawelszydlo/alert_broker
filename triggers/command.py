"""Will trigger an alert if the provided system command will return an error."""

import logging
import re
import subprocess
from .trigger import Trigger


class CommandTrigger(Trigger):

    def __init__(self, alert, command: str, regexp: str = None,
                 negative_regexp: str = None, interval: int = 10):
        super(CommandTrigger, self).__init__(alert, interval)
        self.command = command
        self.regexp = re.compile(regexp) if regexp else None
        self.negative_regexp = (
            re.compile(negative_regexp) if negative_regexp else None)

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

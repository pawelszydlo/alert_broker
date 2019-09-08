"""Main function to start the broker."""

from broker import Broker
from handlers.blink import BlinkHandler
from handlers.command import CommandHandler
from triggers.diskspace import DiskSpaceTrigger
from triggers.random import RandomTrigger

LOW_DISK_SPACE = 'low disk space'


def main():
    """Main."""
    broker = Broker()

    command_trigger = RandomTrigger(
        LOW_DISK_SPACE)
    broker.register_trigger(command_trigger)

    blink_handler2 = BlinkHandler(LOW_DISK_SPACE, color='#00ffff')
    broker.register_handler(blink_handler2)

    command_handler = CommandHandler(
        LOW_DISK_SPACE, command_on='say "on"', command_off='say "off')
    broker.register_handler(command_handler)

    broker.run()


if __name__ == "__main__":
    main()

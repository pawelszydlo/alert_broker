"""Main function to start the broker."""

from broker import Broker
from handlers.blink import BlinkHandler
from triggers.diskspace import DiskSpaceTrigger

LOW_DISK_SPACE = 'low disk space'


def main():
    """Main."""
    broker = Broker()

    command_trigger = DiskSpaceTrigger(
        LOW_DISK_SPACE, path='/', min_free_mb=20000)
    broker.register_trigger(command_trigger)

    blink_handler2 = BlinkHandler(LOW_DISK_SPACE, color='#00ffff')
    broker.register_handler(blink_handler2)

    broker.run()


if __name__ == "__main__":
    main()

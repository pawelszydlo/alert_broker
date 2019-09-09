"""Main function to start the broker."""

from broker import Broker
from handlers.blink import BlinkHandler
from triggers.command import CommandTrigger
from triggers.diskspace import DiskSpaceTrigger

VPN_OFF = 'vpn off'
LOW_DISK_SPACE = 'low disk space'


def main():
    """Main."""
    broker = Broker()

    command_trigger = CommandTrigger(
        VPN_OFF, command='ifconfig', negative_regexp='.*?tun0.*', interval=60)
    broker.register_trigger(command_trigger)

    disk_trigger = DiskSpaceTrigger(
        LOW_DISK_SPACE, path='/', min_free_mb=2048, interval=60 * 30)
    broker.register_trigger(disk_trigger)

    blink_handler1 = BlinkHandler(LOW_DISK_SPACE, color='#00ffff')
    broker.register_handler(blink_handler1)

    blink_handler2 = BlinkHandler(VPN_OFF, color='#ff0000')
    broker.register_handler(blink_handler2)

    broker.run()


if __name__ == "__main__":
    main()

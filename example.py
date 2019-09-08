"""Main function to start the broker."""

from broker import Broker
from handlers.blink import BlinkHandler
from handlers.command import CommandHandler
from triggers.command import CommandTrigger
from triggers.random import RandomTrigger

VPN_OFF = 'vpn off'


def main():
    """Main."""
    broker = Broker()

    command_trigger = CommandTrigger(
        VPN_OFF, command='ifconfig', negative_regexp='.*?tuan0.*')
    broker.register_trigger(command_trigger)

    blink_handler2 = BlinkHandler(VPN_OFF, color='#00ffff')
    broker.register_handler(blink_handler2)


    broker.run()


if __name__ == "__main__":
    main()

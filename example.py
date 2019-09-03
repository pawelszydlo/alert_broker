"""Main function to start the broker."""

import alerts
from broker import Broker
from handlers.blink import BlinkHandler
from triggers.random import RandomTrigger
from triggers.command import CommandTrigger


def main():
    """Main."""
    broker = Broker()

    command_trigger = CommandTrigger(alerts.ALERT_NO_INTERNET, command='ls -z')
    broker.register_trigger(command_trigger)

    blink_handler = BlinkHandler(alerts.ALERT_NO_VPN, color='#ff00ff')
    broker.register_handler(blink_handler)

    blink_handler2 = BlinkHandler(alerts.ALERT_NO_INTERNET, color='#00ffff')
    broker.register_handler(blink_handler2)

    broker.run()


if __name__ == "__main__":
    main()

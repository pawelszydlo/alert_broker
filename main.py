"""Main function to start the broker."""

import alerts
from broker import Broker
from handlers.blink import BlinkHandler
from triggers.random import RandomTrigger


def main():
    """Main."""
    broker = Broker()

    dummy_trigger = RandomTrigger(alerts.ALERT_NO_VPN)
    broker.register_trigger(dummy_trigger)

    dummy_trigger2 = RandomTrigger(alerts.ALERT_NO_INTERNET)
    broker.register_trigger(dummy_trigger2)

    blink_handler = BlinkHandler(alerts.ALERT_NO_VPN, color='#ff00ff')
    broker.register_handler(blink_handler)

    blink_handler2 = BlinkHandler(alerts.ALERT_NO_INTERNET, color='#00ffff')
    broker.register_handler(blink_handler2)

    broker.run()


if __name__ == "__main__":
    main()

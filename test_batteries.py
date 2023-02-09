import unittest

from batteries.nubbin import NubbinBattery
from batteries.spindler import SpindlerBattery

from datetime import datetime

class TestNubbin(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        last_service_date = datetime(2019, 1, 1)
        current_date = datetime(2023, 1, 2)

        battery = NubbinBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):

        last_service_date = datetime(2019, 1, 1)
        current_date = datetime(2022, 12, 31)

        battery = NubbinBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        last_service_date = datetime(2019, 1, 1)
        current_date = datetime(2022, 1, 2)

        battery = SpindlerBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):

        last_service_date = datetime(2019, 1, 1)
        current_date = datetime(2021, 12, 31)

        battery = SpindlerBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
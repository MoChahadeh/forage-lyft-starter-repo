import unittest

from tires.carrigan import CarriganTire
from tires.octoprime import OctoprimeTire


class TestCarrigan(unittest.TestCase):

    def test_tire_should_be_serviced(self):

        sensor_reading = [0.9, 0.8, 0.7, 0.6]

        tire = CarriganTire(sensor_reading)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):

        sensor_reading = [0.8, 0.7, 0.6, 0.5]

        tire = CarriganTire(sensor_reading)

        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):

    def test_tire_should_be_serviced(self):

        sensor_reading = [1,1,0,1]

        tire = OctoprimeTire(sensor_reading)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):

        sensor_reading = [1,1,0.9,0]

        tire = OctoprimeTire(sensor_reading)

        self.assertFalse(tire.needs_service())

if __name__ == "__main__":
    unittest.main()
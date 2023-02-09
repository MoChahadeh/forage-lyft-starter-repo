import unittest


from engines.capulet import CapuletEngine
from engines.sternman import SternmanEngine
from engines.willoughby import WilloughbyEngine


class TestCapulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        last_service_mileage = 20000
        current_mileage = 50001

        engine = CapuletEngine(last_service_mileage, current_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):

        last_service_mileage = 20000
        current_mileage = 49999

        engine = CapuletEngine(last_service_mileage, current_mileage)

        self.assertFalse(engine.needs_service())


class TestSterman(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        warning_light_on = True

        engine = SternmanEngine(warning_light_on)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):

        warning_light_on = False

        engine = SternmanEngine(warning_light_on)

        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):

        last_service_mileage = 20000
        current_mileage = 80001

        engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):

        last_service_mileage = 20000
        current_mileage = 79999

        engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
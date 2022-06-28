import unittest
from datetime import datetime

from model.calliope import *
from model.glissade import *
from model.palindrome import *
from model.rorschach import *
from model.thovex import *

from model.tires.carrigan import *
from model.tires.octoprime import *

class CalliopeTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 100)
        warning_lights_is_on = False
        current_mileage = 0

        car = Calliope(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        warning_lights_is_on = False
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())
 

class GlissadeTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        warning_lights_is_on = False
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0

        car = Glissade(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        warning_lights_is_on = False
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

class PalindromeTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        warning_lights_is_on = False
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0

        car = Palindrome(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        warning_lights_is_on = False
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Palindrome(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = True
        current_mileage = 60001
        last_service_mileage = 0

        car = Palindrome(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 60000
        last_service_mileage = 0

        car = Palindrome(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

class RorschachTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        warning_lights_is_on = False
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0

        car = Rorschach(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        warning_lights_is_on = False
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 0
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

class ThovexTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        warning_lights_is_on = False
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0

        car = Thovex(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        warning_lights_is_on = False
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 0
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_date, warning_lights_is_on)
        self.assertTrue(car.require_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        warning_lights_is_on = False
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(current_mileage, last_service_date, warning_lights_is_on)
        self.assertFalse(car.require_service())

class CarriganTest(unittest.TestCase):
    def test_sum_smaller_than_3(self):
        values = [0.5, 0.5, 0.5, 0.5]
        tire = Carrigan(values)
        self.assertFalse(tire.require_service())

    def test_sum_larger_than_3(self):
        values = [0.8, 0.8, 0.8, 0.8]
        tire = Carrigan(values)
        self.assertFalse(tire.require_service())

    def test_one_larger_than_point9(self):
        values = [0.95, 0.5, 0.5, 0.5]
        tire = Carrigan(values)
        self.assertTrue(tire.require_service())


class OctoprimeTest(unittest.TestCase):
    def test_sum_smaller_than_3(self):
        values = [0.5, 0.5, 0.5, 0.5]
        tire = Octoprime(values)
        self.assertFalse(tire.require_service())

    def test_sum_larger_than_3(self):
        values = [0.8, 0.8, 0.8, 0.8]
        tire = Octoprime(values)
        self.assertTrue(tire.require_service())

    def test_one_larger_than_point9(self):
        values = [0.95, 0.5, 0.5, 0.5]
        tire = Octoprime(values)
        self.assertFalse(tire.require_service())

unittest.main()

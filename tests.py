import unittest
from datetime import datetime

from model.calliope import *
from model.glissade import *
from model.palindrome import *
from model.rorschach import *
from model.thovex import *

class CalliopeTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0

        car = Calliope(current_mileage, last_service_date, False)
        self.assertFalse(car.require_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(current_mileage, last_service_date, False)
        self.assertFalse(car.require_service())



unittest.main()

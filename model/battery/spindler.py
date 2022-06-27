from ..battery_base import Battery

class SpindlerBattery:
    def __init__(self, last_service_date):
        self.battery = Battery(last_service_date.timestamp(), 63072000)

    def require_service(self):
        return self.battery.require_service()


# from datetime import datetime
# battery = SpindlerBattery(datetime.today())
#
# print(battery.require_service())

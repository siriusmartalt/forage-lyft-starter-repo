from .battery.nubbin import NubbinBattery
from .engine.capulet import CapuletEngine
from .model_base import Model

class Thovex:
    def __init__(self, milage, last_service_date, warning_light_is_on):
        self.model = Model(NubbinBattery(last_service_date), CapuletEngine(milage, warning_light_is_on))

    def require_service(self):
        return self.model.require_service()

# from datetime import datetime
#
# model = CalliopeModel(10, datetime.now(), True)

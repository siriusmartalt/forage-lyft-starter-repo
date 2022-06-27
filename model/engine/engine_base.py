class EngineBase:
    def __init__(self, mileage_limit, service_when_warning, milage, warning_light_is_on):
        self.mileage_limit = mileage_limit
        self.warning_light_is_on = warning_light_is_on
        self.service_when_warning = service_when_warning
        self.milage = milage

    def require_service(self):
        return ((self.mileage_limit != -1) and (self.mileage_limit <= self.milage)) or (self.service_when_warning and self.warning_light_is_on)

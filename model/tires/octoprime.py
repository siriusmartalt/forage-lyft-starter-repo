from .tire_base import Tire

class Octoprime:
    def __init__(self, values):
        self.tire = Tire('octoprime', values)

    def require_service(self):
        return self.tire.require_service()

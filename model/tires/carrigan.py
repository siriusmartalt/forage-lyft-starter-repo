from .tire_base import Tire

class Carrigan:
    def __init__(self, values):
        self.tire = Tire('carrigan', values)

    def require_service(self):
        return self.tire.require_service()

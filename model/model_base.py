class Model:
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def require_service(self):
        return self.battery.require_service() and self.engine.require_service()

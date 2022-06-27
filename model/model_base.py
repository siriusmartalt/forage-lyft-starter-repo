class Model:
    def __init__(battery, engine):
        self.battery = battery
        self.engine = engine

    def require_service():
        return self.battery.require_service() and self.engine.require_service()

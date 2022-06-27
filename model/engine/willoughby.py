from ..engine_base import EngineBase

class SternmanEngine:
    def __init__(self, milage, warning_light_is_on):
        self.engine = EngineBase(60000, False, milage, warning_light_is_on)

    def require_service(self):
        return self.engine.require_service()

# engine = SternmanEngine(10, True, 10, True)
# print(engine.require_service())

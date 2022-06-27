class Car:
    def __init__(self, model):
        self.model = model

    def require_service(self):
        return self.model.require_service()

# from datetime import datetime
# model = CalliopeModel(10, datetime.now(), False)
# car = Car(model)
# print(car.require_service())

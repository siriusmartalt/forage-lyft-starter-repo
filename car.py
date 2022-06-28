class Car:
    def __init__(self, model, tires):
        self.model = model
        self.tires = tires

    def needs_service(self):
        return self.model.needs_service() or tires.needs_service()

# model = CalliopeModel(10, datetime.now(), False)
# car = Car(model)

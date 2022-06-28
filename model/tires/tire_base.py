class Tire:
    def __init__(self, brand, values):
        self.brand = brand
        self.values = values

    def require_service(self):
        match self.brand:
            
            case 'carrigan':
                return any(x > 0.9 for x in self.values)

            case 'octoprime':
                return (sum(self.values) >= 3)

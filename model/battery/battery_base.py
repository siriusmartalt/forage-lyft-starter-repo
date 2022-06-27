from datetime import datetime

class Battery:
    def __init__(self, last_service_date, expected_lifetime):
        self.last_service_date = last_service_date
        self.expected_lifetime = expected_lifetime

    def require_service(self):
        return (datetime.now().timestamp() - self.last_service_date) > self.expected_lifetime

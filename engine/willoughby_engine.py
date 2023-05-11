from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.service_limit= 60000

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.service_limit

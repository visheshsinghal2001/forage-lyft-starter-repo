from abc import ABC, abstractmethod
from servicible import Servicible

class Car(Servicible,ABC):
    def __init__(self, engine,battery,tire):
        self.Engine=engine;
        self.Battery=battery;
        self.Tire=tire;

    def needs_service(self):
        return self.Engine.needs_service() or self.Battery.needs_service() or self.Tire.needs_service();

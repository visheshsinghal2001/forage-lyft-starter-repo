from abc import ABC, abstractmethod
from servicible import Servicible

class Car(Servicible,ABC):
    def __init__(self, engine,battery):
        self.Engine=engine;
        self.Battery=battery;

    def needs_service(self):
        return self.Engine.needs_service() or self.Battery.needs_service();

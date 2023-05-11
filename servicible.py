from abc import ABC, abstractmethod


class Servicible(ABC):
    def __init__(self):
       pass
    

    @abstractmethod
    def needs_service(self):
        pass
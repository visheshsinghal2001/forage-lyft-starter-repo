

from battery.splinder import splinder
from battery.nubbin import nubbin
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.Carrigan import Carrigan
from tire.Octoprime import Octoprime


class carFactory:

    @staticmethod
    def create_calliope(current_date,service_date,current_mileage,last_service_mileage):
        engine=CapuletEngine(current_mileage,last_service_mileage)
        battery=splinder(current_date,service_date)
        return Car(engine,battery);
        
    @staticmethod
    def create_Thovex(current_date,service_date,current_mileage,last_service_mileage):
        engine=CapuletEngine(current_mileage,last_service_mileage)
        battery=nubbin(current_date,service_date)
        return Car(engine,battery);


    @staticmethod
    def create_rorschach(current_date,service_date,current_mileage,last_service_mileage):
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        battery=nubbin(current_date,service_date)
        return Car(engine,battery);


    @staticmethod
    def create_glissade(current_date,service_date,current_mileage,last_service_mileage):
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        battery=splinder(current_date,service_date)
        return Car(engine,battery);


    @staticmethod
    def create_pallindrome(current_date,service_date,warning_light_is_on):
        engine=SternmanEngine(warning_light_is_on)
        battery=splinder(current_date,service_date)
        return Car(engine,battery);





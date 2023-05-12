

from battery.splinder import splinder
from battery.nubbin import nubbin
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine



class carFactory:

    @staticmethod
    def create_calliope(current_date,service_date,current_mileage,last_service_mileage):
        return Car(CapuletEngine(current_mileage,last_service_mileage),splinder(current_date,service_date));
    @staticmethod
    def create_Thovex(current_date,service_date,current_mileage,last_service_mileage):
        return Car(CapuletEngine(current_mileage,last_service_mileage),nubbin(current_date,service_date));

    @staticmethod
    def create_rorschach(current_date,service_date,current_mileage,last_service_mileage):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),nubbin(current_date,service_date));

    @staticmethod
    def create_glissade(current_date,service_date,current_mileage,last_service_mileage):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),splinder(current_date,service_date));

    @staticmethod
    def create_pallindrome(current_date,service_date,warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on),splinder(current_date,service_date));




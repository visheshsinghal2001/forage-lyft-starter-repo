from abc import ABC
from datetime import datetime
from Battery import Battery


class splinder(Battery, ABC):
    def __init__(self, current_date,last_service_date):
     self.last_service_date=last_service_date;
     self.current_date=current_date;
     self.year_gap=4;
def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.year_gap)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
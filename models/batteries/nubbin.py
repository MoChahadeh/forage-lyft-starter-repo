from models.battery import Battery
from datetime import datetime

class NubbinBattery(Battery):

    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        return self.current_date > self.last_service_date.replace(year=self.last_service_date.year + 4)
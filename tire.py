from serviceable import Serviceable
from abc import ABC, abstractmethod

class Tire(Serviceable, ABC):

    def __init__(self, sensor_reading: list[float]):
        self.sensor_reading = sensor_reading
    
    @abstractmethod
    def needs_service(self):
        pass
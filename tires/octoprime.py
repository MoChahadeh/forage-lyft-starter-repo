from tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, sensor_reading: list[float]) -> None:
        super().__init__(sensor_reading)
    
    def needs_service(self) -> bool:
        return sum(self.sensor_reading) >= 3

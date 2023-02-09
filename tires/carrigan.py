from tire import Tire


class CarriganTire(Tire):

    def __init__(self, sensor_reading: list[float]) -> None:
        super().__init__(sensor_reading)

    def needs_service(self) -> bool:
        return len([x for x in self.sensor_reading if x >= 0.9]) > 0
from abc import ABC, abstractmethod
from models.serviceable import Serviceable
from models.engine import Engine
from models.battery import Battery


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine:Engine  = engine
        self.battery:Battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

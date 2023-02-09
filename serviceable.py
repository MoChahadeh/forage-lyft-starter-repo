from abc import ABCMeta, abstractmethod


class Serviceable(metaclass=ABCMeta):
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass
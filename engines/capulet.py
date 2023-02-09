from engine import Engine

class CapuletEngine(Engine):

    def __init__(self, last_service_milage: int, current_milage: int) -> None:
        self.last_service_milage = last_service_milage
        self.current_milage = current_milage
    
    def needs_service(self) -> bool:
        return self.current_milage - self.last_service_milage > 30000
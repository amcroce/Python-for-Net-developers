import abc

class Car(metaclass=abc.ABCMeta):
    def __init__(self, model_name, engine_type, cylinders, base_price):
        self.model_name : str = model_name
        self.engine_type : str = engine_type
        self.cylinders : int = cylinders
        self.base_price : float = base_price

    def is_electric(self) -> bool:
        return self.engine_type == "electric"

    @abc.abstractmethod
    def drive(self):
        print(f"Car: The {self.model_name} goes vroom!")

    @abc.abstractmethod
    def refuel(self):
        pass
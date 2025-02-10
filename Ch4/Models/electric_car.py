from Models.car import Car

class ElectricCar(Car):

    def __init__(self, model_name, base_price):
        super().__init__(model_name, 'electric', 0, base_price)

    def drive(self):
        print(f"ElectricCar: The {self.model_name} zooms silentrly along!")

    def refuel(self):
        print(f"ElectricCar: The {self.model_name} is charging on.")
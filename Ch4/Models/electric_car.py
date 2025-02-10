from Models.car import Car

class ElectricCar(Car):
    def drive(self):
        print(f"ElectricCar: The {self.model_name} zooms silentrly along!")

    def refuel(self):
        print(f"ElectricCar: The {self.model_name} is charging on.")
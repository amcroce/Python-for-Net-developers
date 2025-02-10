from typing import List
from Models.basic_car import BasicCar
from Models.car import Car
from Models.electric_car import ElectricCar
from Models.sports_cart import SportsCar


def main():
    cars = create_cars()
    for car in cars:
        print(f"{car.model_name} is electric? {car.is_electric}")
        car.drive()
        car.refuel()
        print()
    pass

def create_cars() -> List[Car]:
    return [
        SportsCar('Corvette', 'gas', 8, 50.000),
        BasicCar('Windstar', 'gas', 6, 20.000),
        ElectricCar('Tesla', 60.000),
        ElectricCar('Bolt', 40.000),
    ]

if __name__ == "__main__":
    main()
from typing import List
from Models.parking_lot import ParkingLot
from Models.basic_car import BasicCar
from Models.car import Car
from Models.electric_car import ElectricCar
from Models.sports_cart import SportsCar


def main():
    cars = create_cars()
    use_cars(cars)

    lot = ParkingLot.create(5, 3)
    print("Free spots:")
    for spot in lot:
        print(spot)

    park_cars(cars, lot)
    print("Taken spots:")
    for spot in lot.taken_spots():
        print(spot)
    pass

def park_cars(cars: List[Car], lot: ParkingLot):
    for car in cars:
        lot.park_car(car)
    print()
    pass

def use_cars(cars):
    for car in cars:
        print(f"{car.model_name} is electric? {car.is_electric}")
        car.drive()
        car.refuel()
        print()

def create_cars() -> List[Car]:
    return [
        SportsCar('Corvette', 'gas', 8, 50.000),
        BasicCar('Windstar', 'gas', 6, 20.000),
        ElectricCar('Tesla', 60.000),
        ElectricCar('Bolt', 40.000),
    ]

if __name__ == "__main__":
    main()
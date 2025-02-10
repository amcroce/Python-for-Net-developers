from Models.car import Car


def main():
    cars = create_cars()
    for car in cars:
        car.drive()
        car.refuel()
    pass

def create_cars():
    return [
        Car('Corvette', 'gas', 8, 50.000),
        Car('Windstar', 'gas', 6, 20.000),
        Car('Tesla', 'electric', 0, 60.000),
        Car('Bolt', 'electric', 0, 40.000),
    ]

if __name__ == "__main__":
    main()
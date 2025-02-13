from typing import Iterator
from Models.car import Car

class ParkingLot:
    def __init__(self, names: list[str]):
        # Here I initialize with a kind of lambda. I use {} because is a dictionary (key-value pairs)
        self.__spots: dict[str, Car] = {name: None for name in names}
        self.__spot_names = list(self.__spots.keys())

    @staticmethod
    def create(sptsPerLevel: int, levels: int) -> "ParkingLot":
        names : list[str] = []
        level_names : list[str] = ["A", "B", "C", "D", "E", "F", "G"]
        for ln in level_names[:levels]:
            for spot in range(sptsPerLevel):
                names.append(f"{ln}{spot+1}")
        return ParkingLot(names)

    def taken_spots(self) -> list[str]:
        return [f"{spot} has the {car.model_name}" for spot, car in self.__spots.items() if car is not None]

    def park_car(self, car: Car):
        for spot in self.__spots:
            if self.__spots[spot] is None:
                self.__spots[spot] = car
                break

    def __iter__(self) -> Iterator[str]:
        self.__iter_index = 0
        return self

    def __next__(self) -> str:
        if self.__iter_index < len(self.__spot_names):
            spot = self.__spot_names[self.__iter_index]
            self.__iter_index += 1
            return spot
        else:
            raise StopIteration


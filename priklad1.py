from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def consumption(self):
        pass


class CombustionCar(Car):
    def __init__(self, brand, model, fuel_consumption):
        super().__init__(brand, model)
        self.fuel_consumption = fuel_consumption

    def consumption(self):
        return self.fuel_consumption

if __name__ == "__main__":
    car = CombustionCar("ford", "fokus", 100)
    print(car.consumption())

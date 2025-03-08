from abc import ABC, abstractmethod

class Animal(ABC):
    @staticmethod
    def domestic_factory(animal_name):
        pass
    @staticmethod
    def wild_factory(animal_name):
        pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass


if __name__ == "__main__":
    animal1 = Animal.domestic_factory("dog")
    animal2 = Animal.domestic_factory("cat")
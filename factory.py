from abc import ABC, abstractmethod

"""
 Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
"""

class Burger(ABC):
    @abstractmethod
    def create(self):
        pass


class CheeseBurger(Burger):
    def create(self):
        print("CheeseBurger")


class VegBurger(Burger):
    def create(self):
        print("VegBurger")


class ChickenBurger(Burger):
    def create(self):
        print("ChickenBurger")


class BurgerFactory:

    @staticmethod
    def create_burger(burger_type):
        if burger_type == "cheese":
            return CheeseBurger()
        if burger_type == "veg":
            return VegBurger()
        if burger_type == "chicken":
            return ChickenBurger()

    


burgers = BurgerFactory()

veg_burger = BurgerFactory.create_burger('chicken')
veg_burger.create()
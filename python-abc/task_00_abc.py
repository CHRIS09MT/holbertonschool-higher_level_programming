from abc import ABC, abstractmethod

"""
Abstract class that represents an animal
"""


class Animal(ABC):
    """
    Abstract method that must be implemented by subclasses
    """

    @abstractmethod
    def sound(self):
        pass


"""
Class that represents a dog, inherits from Animal
"""


class Dog(Animal):
    """
    Implements the sound method, returns "Bark"
    """

    def sound(self):
        return "Bark"


"""
Class that represents a cat, inherits from Animal
"""


class Cat(Animal):
    """
    Implements the sound method, returns "Meow"
    """

    def sound(self):
        return "Meow"

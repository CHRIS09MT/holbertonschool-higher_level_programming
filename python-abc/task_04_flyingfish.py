"""Module provides definition of Fish, Bird and FlyingFish classes"""


class Fish:
    """The definition of the Fish class"""

    def swim(self):
        """prints a message to the console"""
        print("The fish is swimming")

    def habitat(self):
        """prints a message to the console"""
        print("The fish lives in water")


class Bird:
    """The definition of the Bird class"""

    def fly(self):
        """prints a message to the console"""
        print("The bird is flying")

    def habitat(self):
        """prints a message to the console"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """defines a FlyingFish"""

    def fly(self):
        """prints a message to the console"""
        print("The flying fish is soaring!")

    def swim(self):
        """prints a message to the console"""
        print("The flying fish is swimming!")

    def habitat(self):
        """prints a message to the console"""
        print("The flying fish lives both in water and the sky!")

class SwimMixin:
    """Mixin class to add swimming behavior."""

    def swim(self):
        """Prints a message indicating the creature swims."""

        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying behavior."""

    def fly(self):
        """Prints a message indicating the creature flies."""

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly."""

    def roar(self):
        """Prints a message indicating the dragon roars."""

        print("The dragon roars!")

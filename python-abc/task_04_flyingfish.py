class Fish:
    """
    Represents a fish with swimming abilities.
    """

    def swim(self):
        """
        Make the fish swim.
        """

        print("The fish is swimming")

    def habitat(self):
        """
        Describe the fish's habitat.
        """

        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying abilities.
    """

    def fly(self):
        """
        Make the bird fly.
        """

        print("The bird is flying")

    def habitat(self):
        """
        Describe the bird's habitat.
        """

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that can both swim and fly.
    """

    def fly(self):
        """
        Make the flying fish soar through the air.
        """

        print("The flying fish is swimming!")

    def swim(self):
        """
        Make the flying fish swim.
        """

        print("The flying fish is soaring!")

    def habitat(self):
        """
        Describe the flying fish's habitat in both water and the sky.
        """

        print("The flying fish lives both in water and the sky!")

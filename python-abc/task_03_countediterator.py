class CountedIterator:
    """
    Iterator that keeps track of how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize with an iterable and set the count to 0.
        """

        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Return the current count of iterated items.
        """

        return self.count

    def __next__(self):
        """
        Return the next item and increment the count.
        """

        try:
            item = next(self.iterable)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Return the iterator itself.
        """

        return self

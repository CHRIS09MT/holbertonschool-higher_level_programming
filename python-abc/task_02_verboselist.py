class VerboseList(list):
    """
    Subclass of list that prints notifications for list operations.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.
        """

        print(f"Added {item} to the list.")
        super().append(item)

    def extend(self, item):
        """
        Extend the list with items from an iterable and print a notification.
        """

        print(f"Extended the list with {len(item)} items.")
        super().extend(item)

    def remove(self, item):
        """
        Remove the first occurrence of an item and print a notification.
        """

        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, item=-1):
        """
        Pop an item from the list and print a notification.
        """

        item = super().pop(item)
        print(f"Popped {item} from the list.")
        return item

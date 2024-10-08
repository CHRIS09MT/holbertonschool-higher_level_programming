"""
Importing pickle
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes in readable format.
        """

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current CustomObject instance and save to a file.
        """

        with open(filename, "wb") as file:
            try:
                pickle.dump(self, file)
            except pickle.PicklingError as e:
                print(f"{e}")
                return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a file and returns a CustomObject instance.
        """
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
                if isinstance(data, cls):
                    return data
                else:
                    return None
        except (pickle.UnpicklingError, EOFError, FileNotFoundError, IOError) as e:
            print(f"{e}")
            return None

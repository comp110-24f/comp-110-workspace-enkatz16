"""File to define Fish class."""

__author__: str = "730748249"


class Fish:
    """Creating a class for fish."""

    age: int

    def __init__(self):
        """Assigning an age of 0 on creation."""
        self.age = 0
        return None

    def one_day(self):
        """Increasing age by one every day."""
        self.age += 1
        return None

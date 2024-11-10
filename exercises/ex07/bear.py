"""File to define Bear class."""

__author__: str = "730748249"


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Assign age 0 and hunger score 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase age by one and remove hunger by one."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase hunger score if a fish is eaten."""
        self.hunger_score += num_fish
        return None

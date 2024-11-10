"""File to define River class."""

__author__: str = "730748249"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creating a class for the river at large."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish and bears if they are too old."""
        new_fish: list[Fish] = []
        for item in self.fish:
            if item.age <= 3:
                new_fish.append(item)
        self.fish = new_fish
        new_bears: list[Bear] = []
        for item in self.bears:
            if item.age <= 5:
                new_bears.append(item)
        self.bears = new_bears
        return None

    def bears_eating(self):
        """Bears eating fish and adjusting hunger."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(amount=3)
                bear.eat(num_fish=3)
        return None

    def check_hunger(self):
        """If a bear is too hungry, it is removed."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Reproduction of fish."""
        additional_fish: int = 0
        if len(self.fish) % 2 == 0:
            additional_fish = int((len(self.fish) / 2) * 4)
        else:
            additional_fish = int(((len(self.fish) - 1) / 2) * 4)
        for fish in range(additional_fish):
            new_fish: Fish = Fish()
            self.fish.append(new_fish)
        return None

    def repopulate_bears(self):
        """Reproduction of bears."""
        new_bears: int = 0
        if len(self.bears) % 2 == 0:
            new_bears = int(len(self.bears) / 2)
        else:
            new_bears = int((len(self.bears) - 1) / 2)
        for bear in range(new_bears):
            new_bear: Bear = Bear()
            self.bears.append(new_bear)
        return None

    def view_river(self):
        """Visualize the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Increasing the river by one week by processing seven days."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Removing fish if they are eaten."""
        index: int = 0
        while index < amount:
            self.fish.pop(0)
            index += 1
        return None

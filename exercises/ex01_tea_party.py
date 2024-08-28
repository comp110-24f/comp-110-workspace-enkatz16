"""Plan a tea party's tea bags, treats, and cost based on the number of guests."""

__author__: str = "730748249"


def main_planner(guests: int) -> None:
    """Find the final number of tea bags, treats, and cost."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # changing function output from int to str for concatenation
    print(
        "Treats: " + str(treats(guests))
    )  # changing function output from int to str for concatenation
    print(
        "Cost: $" + str(cost((tea_bags(guests)), treats(guests)))
    )  # change from float to str to print and concatenate


def tea_bags(people: int) -> int:
    """Determine the tea bags necessary for the party based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Determine the number of treats necessary for the party based on the number of teas people drink."""
    return round(
        (tea_bags(people=people) * 1.5)
    )  # using round function to get numbers in whole tea bags since one cannot buy half a teabag


def cost(tea_count: int, treat_count: int) -> float:
    """Find the cost of the party based on the amount of tea and treats needed."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# String Analogy
my_name: str = ""  # literal for a string
my_name: str = str()  # constructor for a string

# Adding a value to a list
index: int = 0
my_numbers.append(1.5)
print(my_numbers)

game_points: list[int] = [102, 86, 94, 86, 32, 34, 64]
game_points[1] = 72
print(len(game_points))
game_points.pop(1)
print(game_points)


def display(input_list: list[int]) -> None:
    index: int = 0
    while index <= len(input_list) - 1:
        print(input_list[index])
        index += 1


display(game_points)

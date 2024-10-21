"""Building list utility functions"""

__author__ = "730748249"


def only_evens(integers: list[int]) -> list[int]:
    even_list: list[int] = []
    for element in range(0, len(integers)):
        if integers[element] % 2 == 0:
            even_list.append(integers[element])
    return even_list


def sub(original: list[int], start_index: int, end_index: int) -> list[int]:
    modified_list: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index >= len(original):
        end_index = len(original)
    for element in range(start_index, end_index):
        modified_list.append(original[element])
    return modified_list


def add_at_index(integers: list[int], element: int, user_index: int) -> None:
    index: int = 0
    if user_index > len(integers) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    integers.append(element)
    while index < len(integers) - user_index - 1:
        temporary: int = integers[user_index]
        integers.pop(user_index)
        integers.append(temporary)
        index = index + 1

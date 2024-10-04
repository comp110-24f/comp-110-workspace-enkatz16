"""Exercise for lists and functions"""

__author__: str = "730748249"


def all(number_list: list[str], number: int) -> bool:
    all_number: bool = True
    index: int = 0
    while index < len(number_list):
        if list[index] != number:
            all_number = False
        index += 1
    return all_number


def max(integer_list: list[int]) -> int:
    if len(integer_list) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max: int = integer_list[0]
    while index < len(integer_list):
        if integer_list[index] > max:
            max = integer_list[index]
        index += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    equal: bool = True
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            equal = False
        index += 1
    return equal


def extend(list_1: list[int], append_list: list[int]) -> None:
    index: int = 0
    while index < len(append_list):
        list_1.append(append_list[index])
        index += 1

"""Mutating functions."""

__author__: str = "730748249"


def manual_append(set_list: list[int], appending_int: int) -> None:
    set_list.append(appending_int)


def double(doubling_list: list[int]) -> None:
    index: int = 0
    while index < len(doubling_list):
        doubling_list[index] = doubling_list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)

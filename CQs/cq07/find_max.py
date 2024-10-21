"""Defining a function to find and remove maximum values for a list, to be tested"""

__author__: str = "730748249"


def find_and_remove_max(integers: list[int]) -> int:
    """Find and remove the maximum value from a list"""
    index: int = 0
    maximum: int = -1
    for element in integers:
        if element > maximum:
            maximum = element
    while index < len(integers):
        if integers[index] == maximum:
            integers.pop(index)
        else:
            index += 1
    return maximum

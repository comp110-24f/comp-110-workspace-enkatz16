"""Exercise for lists and functions"""

__author__: str = "730748249"


def all(number_list: list[int], number: int) -> bool:
    """Matches a list to the number defined"""
    all_number: bool = True
    if len(number_list) == 0:
        all_number = False
    # set it to true to start, only return false if it finds something not equal
    # or if there are no numbers
    # need the prior conditional to make sure no empty lists
    index: int = 0
    while index < len(number_list):
        if number_list[index] != number:
            all_number = False
        index += 1
        # keep this outside of the conditional
    return all_number


def max(integer_list: list[int]) -> int:
    """Finds the max of a list of numbers"""
    if len(integer_list) == 0:
        raise ValueError("max() arg is an empty List")
    # using this conditional since it returns an int instead of bool
    index: int = 0
    max: int = integer_list[0]
    while index < len(integer_list):
        if integer_list[index] > max:
            max = integer_list[index]
        index += 1
    return max
    # return so function ends


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if two lists contain the same values in the same order"""
    index: int = 0
    equal: bool = True
    # initialize as true, set as false if not
    if len(list_1) != len(list_2):
        equal = False
        return equal
    # end early if the list lengths aren't the same
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            equal = False
        index += 1
    # only set it equal to false, since it'll be troublesome to match 3 conditions
    # vs just one
    return equal


def extend(list_1: list[int], append_list: list[int]) -> None:
    """Appends one list to the end of another"""
    index: int = 0
    while index < len(append_list):
        list_1.append(append_list[index])
        index += 1

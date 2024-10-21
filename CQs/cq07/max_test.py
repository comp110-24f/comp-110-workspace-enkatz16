"""Testing the max function"""

__author__: str = "730748249"

from cq07.find_max import find_and_remove_max

list_a: list[int] = [10, 9, 8, 7, 10]


def test_return() -> None:
    """Test to make sure it returns the correct value"""
    list_a: list[int] = [10, 9, 8, 7, 10]
    assert find_and_remove_max(integers=list_a) == 10


def test_mutation() -> None:
    """Make sure that the function mutates a list correctly"""
    list_b: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(integers=list_b)
    assert list_b == [9, 8, 7]


def test_unconventional() -> None:
    """Make sure the function returns -1 on an empty list"""
    list_c: list[int] = []
    assert find_and_remove_max(integers=list_c) == 0

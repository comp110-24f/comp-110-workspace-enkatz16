"""Building list utility functions"""

__author__ = "730748249"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_empty_import() -> None:
    """if the even list is empty, return an empty list"""
    list_a: list[int] = []
    assert only_evens(list_a) == []


def test_only_evens_nonmutation() -> None:
    """ensure that the original list is not changed at all"""
    list_b: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    only_evens(list_b)
    assert list_b == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_only_evens_return() -> None:
    """make sure that the function returns the right value"""
    list_c: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(list_c) == [2, 4, 6, 8, 10]


def test_sub_empty_import() -> None:
    """ensure that an empty list is returned if the import list is empty"""
    list_d: list[int] = []
    assert sub(list_d, 1, 3) == []


def test_sub_mutation() -> None:
    """ensure that the original list is not mutated"""
    list_e: list[int] = [1, 2, 3, 4, 5]
    sub(list_e, 1, 2)
    assert list_e == [1, 2, 3, 4, 5]


def test_sub_return() -> None:
    """ensure that the function returns the right value"""
    list_f: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_f, 1, 3) == [2, 3]


def test_add_at_index_empty_list() -> None:
    """if a list is empty, just add the single value"""
    list_g: list[int] = []
    add_at_index(list_g, 0, 0)
    assert list_g == [0]


def test_add_at_index_mutation() -> None:
    """ensure that the list grows by 1 value after using a function"""
    list_h: list[int] = [1, 2, 4, 5]
    add_at_index(list_h, 2, 3)
    assert len(list_h) == 5


def test_add_at_index_return() -> None:
    """ensure that the function works correctly"""
    list_i: list[int] = [1, 2, 4, 5]
    add_at_index(list_i, 3, 2)
    assert list_i == [1, 2, 3, 4, 5]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    list_j: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(list_j, 3, 3)

"""Testing list functions"""

from lessons.unit_tests.list_fns import get_first, remove_first


def test_get_first() -> None:
    """get_first should return first element."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


def test_remove_first_behavior() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == ["golden", "poodle", "lab"]

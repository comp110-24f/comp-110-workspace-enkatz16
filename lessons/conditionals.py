"""Practice with conditionals"""


def less_than_10(num: int) -> bool:
    """Tell me if num is < 10."""
    if num < 10:
        return True
    else:
        return False


def less_than_10_size(num: int) -> None:
    """Tell me if num < 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hello", letter="h"))

"""Practice with conditionals"""

import random


def less_than_ten(num: int) -> None:
    """Tell me if num is < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_ten(num=5)


def random_statistics(num: int) -> None:
    """Give random stats about a number"""
    print(num)
    if num == 0:
        print("Zero is neither even nor odd.")
    elif (num % 2) == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
    if num > 0:
        print("Number is positive.")
    elif num < 0:
        print("Number is negative.")
    else:
        print("Zero is neither positive nor negative.")


random_statistics(random.randrange(-10, 10))'
'
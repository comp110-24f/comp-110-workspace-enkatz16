"""Third CQ of the semester!"""

__author__: str = "730748249"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    instances: int = 0
    while count < len(phrase):
        if search_char == phrase[count]:
            instances = instances + 1
        count = count + 1
    return instances

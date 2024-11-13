"""Work with linked lists in Python."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def sum(head: Node | None) -> int:
    if head is None:
        return 0
    else:
        rest: int = sum(head.next)
        return rest + head.value


def to_str(head: Node | None) -> str:
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base case: when head is last node (return its value)
    # recursive case: pass it down the list to ask
    if head.next is None:
        return head.value
    else:
        rest: int = last(head.next)
        return rest


print(last(two))
print(last(one))
print(last(courses))

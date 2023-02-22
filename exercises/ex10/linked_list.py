"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730477174"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        

def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else: 
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:  
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else: 
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the value at a specific index in a linked list, or raises a ValueError if the list is empty."""
    i: int = index
    if head is None:
        raise ValueError("Index is out of bounds on the list.")
    else:
        if i != 0:
            i = i - 1
            return value_at(head.next, i)
        else:
            return head.data
    

def max(head: Optional[Node]) -> int:
    """Returns the maximum data value in a Linked List, if the list is empty, it will return a ValueError."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next is None:
            return head.data
        else:
            p = max(head.next)
            if head.data > p:
                p = head.data
                return head.data
            else: 
                return p


def linkify(items: list[int]) -> Optional[Node]: 
    """Returns a linked list of Nodes with the same values, in the same order, as the input list."""
    if len(items) == 0:
        return None
    elif len(items) == 1:
        return Node(items[0], None)
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new linked list of Nodes where each value in the original list is multiplied by the scaling factor."""
    if head is None:
        return None
    if head.next is None:
        return Node(head.data * factor, None)
    else:
        return Node(head.data * factor, scale(head.next, factor))

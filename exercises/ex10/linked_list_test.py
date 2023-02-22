"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, max, value_at, linkify, is_equal, scale

__author__ = "730477174"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise a value error."""
    with pytest.raises(ValueError):
        value_at(None, 0)


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty list should return a reference to the data within the node at the specified index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_empty() -> None:
    """Max of an empty list should raise a value error."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Max of a non-empty list should return a reference to the greatest value of data in the Linked List."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_linkify_empty() -> None:
    """Linkify of an empty list should return None."""
    list1: list[int] = []
    assert linkify(list1) is None


def test_linkify_non_empty() -> None:
    """Linkify of a non-empty list should return a Linked list of nodes with the same value in the same order as the imput list."""
    list2: list[int] = [1, 2, 3, 4]
    assert is_equal(linkify(list2), Node(1, Node(2, Node(3, Node(4, None)))))


def test_scale_empty() -> None:
    """Tests a base case scenario where no head argument is given, should return None."""
    assert is_equal(scale(None, 2), None)


def test_scale_non_empty() -> None:
    """Tests a recursion case scenario where the function creates a new Node with its original data numbers multiplied by the arguement numbers given."""
    assert is_equal(scale(Node(1, Node(2, None)), 2), Node(2, Node(4, None)))
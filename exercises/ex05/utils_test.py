"""EX05- List Utility Functions// Function Tester."""

__author__ = """730477174"""


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_fringe() -> None:
    """Tests a fringe scenario for only_evens."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_real_one() -> None:
    """Tests an actual use scenario for only_evens."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_real_two() -> None: 
    """Tests another actual use case for only_evens. Test includes result when only 1 list item is even."""
    xs: list[int] = [11, 9, 8]
    assert only_evens(xs) == [8]


def test_sub_fringe() -> None:
    """Tests a fringe case of sub function where the list is empty."""
    xs: list[int] = []
    assert sub(xs, 2, 4) == []


def test_sub_real_one() -> None: 
    """Tests a real case of sub function. This is a normal use case."""
    assert sub([7, 9, 11, 22, 24, 16], 1, 5) == [9, 11, 22, 24]


def test_sub_real_two() -> None:
    """Tests a real case of sub function. Here there is a negative x argument and a y arguement that is < the len of the list."""
    ps: list[int] = [9, 17, 19, 25, 18]
    assert sub(ps, -1, 21) == [9, 17, 19, 25, 18]


def test_concat_fringe() -> None:
    """Tests a fringe case scenario of the concat function."""
    po: list[int] = []
    lo: list[int] = []
    assert concat(po, lo) == []


def test_concat_real_one() -> None:
    """Tests a completely normal use case of concat."""
    il: list[int] = [1, 2, 3, 4]
    ip: list[int] = [5, 6, 7, 8]
    assert concat(il, ip) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_real_two() -> None:
    """Tests a use case of concat in which both lists contain similar ints."""
    assert concat([9, 11, 12, 13, 14], [12, 14, 18, 19]) == [9, 11, 12, 13, 14, 12, 14, 18, 19]
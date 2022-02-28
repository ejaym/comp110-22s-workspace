"""EX06- Dictionary Functions Tests."""

__author__ = """730477174"""


from dictionary import favorite_color, invert, count


def test_invert_one() -> None:
    """Tests a normal use case of the invert function."""
    food: dict[str, str] = {"Pies": "Pizza", "Cows": "Burgers"}
    assert invert(food) == {"Pizza": "Pies", "Burgers": "Cows"}


def test_invert_fringe() -> None:
    """Tests a fringe use case of the invert function where a key error occurs."""
    assert invert({"Play": " "}) == {" ": "Play"}


def test_invert_two() -> None:
    """Tests another normal use case of the invert function."""
    Names: dict[str, str] = {"Joe": "Mama", "Jeff": "Bezos", "Evan": "Junior"}
    assert invert(Names) == {"Mama": "Joe", "Bezos": "Jeff", "Junior": "Evan"}


def test_favorite_color_one() -> None:
    """Tests the favorite_color function in a normal use case."""
    colors: dict[str, str] = {"Joe": "blue", "Mary": "blue", "Mama": "green", "Dad": "red"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_fringe() -> None:
    """Tests the favorite_color function fringe case scenario, in the event of a tie."""
    colors: dict[str, str] = {"Joe": "red", "Mary": "blue", "Mama": "yellow"}
    assert favorite_color(colors) == "red"


def test_favorite_color_two() -> None:
    """Tests the favorite_color function in a normal use case."""
    colors: dict[str, str] = {"Obama": "Purple", "Red": "Red", "Purple": "Purple"}
    assert favorite_color(colors) == "Purple"


def test_count_one() -> None: 
    """Tests the count function in a normal use case."""
    assert count(["These", "Big", "Plop", "These"]) == {"These": 2, "Big": 1, "Plop": 1}


def test_count_fringe() -> None:
    """Tests a fringe case use of count."""
    assert count([""]) == {"": 1}


def test_count_two() -> None:
    """Tests another normal use case of count."""
    assert count(["wow", "wow", "wow", "wow", "wow"]) == {"wow": 5}
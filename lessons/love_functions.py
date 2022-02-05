"""Examples of loving definitions <3"""


def love(name: str) -> str:
    """Given a name as a parameter, returns a love string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    love_note: str = ""
    love_counter: int = 0
    while love_counter < n:
        love_counter += 1
        love_note += love(to) + "\n"
    return love_note
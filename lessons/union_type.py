"""An example of Union types."""


from typing import Union


def log(info: Union[int, str] = "OHNO") -> None:
    """log is a function that can be called with either an int or str argument."""
    if isinstance(info, str):
        print(f"str: {info.lower()}")
    else:
        print(f"int: {info}")


log()
log("Hello, World")
log(110)
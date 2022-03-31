from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatentation operator."""
        result_list: list[str] = []

        if isinstance(rhs, str):
            for items in self.items:
                result_list.append(items + rhs)
        else: 
            assert len(self.items) == len(rhs.items)
            for i in range(0, len(self.items)):
                result_list.append(self.items[i] + rhs.items[i])

        return StrArray(result_list)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + " " + last)
print(last)
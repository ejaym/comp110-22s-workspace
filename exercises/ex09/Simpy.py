"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730477174"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes a list of floats that becomes Simpy."""
        self.values = values
    
    def __str__(self) -> str:
        """Allows for Simpy to be printed in a way humans can read."""
        return f"Simpy({self.values})"
    
    def fill(self, number: float, times: int) -> None:
        """Repeats a number for the specified amount of times within Simpy."""
        self.values = []
        i: int = 0
        while len(self.values) < times:
            self.values.append(number)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        """Counts up or down from start value to stop value by the step specified."""
        assert step != 0
        self.values = []
        i: int = 0

        while step > 0 and (start + step * i) < stop:
            self.values.append(start + step * i)
            i += 1

        i = 0

        while step < 0 and (start + step * i) > stop:
            self.values.append(start + step * i)
            i += 1

    def sum(self) -> float:
        """Adds all values of a Simpy together."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Vectorized concatentation operator."""
        result_list: list[float] = []

        if isinstance(rhs, float):
            for values in self.values:
                result_list.append(values + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_list.append(self.values[i] + rhs.values[i])

        return Simpy(result_list)
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Operator overload that allows for simpy to be exponentialized."""
        result_list: list[float] = []

        if isinstance(rhs, float):
            for values in self.values:
                result_list.append(values ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_list.append(self.values[i] ** rhs.values[i])

        return Simpy(result_list)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Returns a list of bools that determines whether or not the input is equal to a specified float."""
        result_list: list[bool] = []
        i: int = 0

        if isinstance(rhs, float):
            while i < len(self.values):
                result_list.append(self.values[i] == rhs)
                i += 1
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_list.append(self.values[i] == rhs.values[i])

        return result_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools that determinds whether the Simpy is greater than the input comparison."""
        result_list: list[bool] = []
        i: int = 0

        if isinstance(rhs, float):
            while i < len(self.values):
                result_list.append(self.values[i] > rhs)
                i += 1
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result_list.append(self.values[i] > rhs.values[i])
        
        return result_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:  # TODO FIX THIS LOL
        """Returns a float value at the index of Simpy specified."""
        result_list: list[float] = []
        i: int = 0

        if isinstance(rhs, int):
            assert 0 <= rhs < len(self.values)
            return self.values[rhs]
        else: 
            assert len(self.values) == len(rhs)
            for i in range(0, len(self.values)):
                if rhs[i] is True:
                    result_list.append(self.values[i])
        
        return Simpy(result_list)
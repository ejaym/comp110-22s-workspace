"""EX05- List Utility Functions// Skeleton Functions."""

__author__ = """730477174"""


def only_evens(int_list: list[int]) -> list[int]:
    """Returns a list of only even ints."""
    i: int = 0
    even_list: list[int] = []
    while i < len(int_list):
        if (int_list[i] % 2) == 1:  # If the number at index i is anything other than an even number it will be ignored and not added to the new even list.
            i += 1
        else:
            even_list.append(int_list[i])  # Even numbers are added to this new list.
            i += 1
    return even_list


def sub(list_ints: list[int], x: int, y: int) -> list[int]:
    """Returns a list of numbers between the specified indecies."""
    i: int = 0
    called_list_ints: list[int] = []
    if y > len(list_ints):  # This if statement takes care of y values that are greater than the total index of the list.
        y == len(list_ints)
    if x < len(list_ints):  # This statement takes care of negative x values and sets them equal to the first index of the list.
        x == 0
    while i < len(list_ints):
        if i >= x and i < y:
            called_list_ints.append(list_ints[i])  # This statement adds the specified ints to a new list that is returned to the user.
        i += 1
    return called_list_ints


def concat(first_int_list: list[int], second_int_list: list[int]) -> list[int]:
    """Creates a new list: the first list immediately followed with the second list."""
    i: int = 0
    y: int = 0
    concated_list: list[int] = []
    total_len: int = len(first_int_list) + len(second_int_list)  # total_len tells the while loop when to stop cycling through itself and ensures that this function will work no matter the legnth of the lists.
    while i < total_len:
        if i < len(first_int_list):
            concated_list.append(first_int_list[i])  # Adds the ints of the first list to the list first.
            i += 1
        elif i >= len(first_int_list) and i < total_len:
            concated_list.append(second_int_list[y])  # I use a new variable of y here in order to ensure that the correct indecies are accessed when adding the second list to the first list.
            i += 1
            y += 1
    return concated_list
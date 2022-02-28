"""EX06- Dictionary Functions."""

__author__ = """730477174"""


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key and the value of a dictionary."""
    invert_dict: dict[str, str] = {}
    new_keys: list[str] = list()
    new_values: list[str] = list()
    y: int = 0
    for i in input_dict:
        new_keys.append(input_dict[i])  # Here the values of the dictionary are added to a list that will be the new keys.
        new_values.append(i)  # Here the keys of the dictionary are added to a list that will be the new values.
    for j in new_keys:
        if new_keys.count(j) != 1:  # If there is a key with the same name it will raise a key error.
            raise KeyError("Repeated Key.")
    while y < len(input_dict):
        invert_dict[new_keys[y]] = new_values[y]  # This assigns an empty dictionary the key value list at index y and assigns its value to be the new value of the list that was just created at y.
        y += 1
    return invert_dict


def favorite_color(input_dict: dict[str, str]) -> str:  # Make it so that this function will return the first min if there is a tie.
    """Returns the most frequently found color value."""
    mentioned_colorss: dict[str, int] = {}
    for i in input_dict:
        if input_dict[i] in mentioned_colorss:
            mentioned_colorss[input_dict[i]] += 1
        else:
            mentioned_colorss[input_dict[i]] = 1
    max_number: int = 0
    max_number_key: str = ""
    for p in mentioned_colorss:
        if mentioned_colorss[p] > max_number:
            max_number = mentioned_colorss[p]
            max_number_key = p
    return max_number_key


def count(input_list: list[str]) -> dict[str, int]: 
    """Counts the amount of time a word appears in a list."""
    return_dict: dict[str, int] = {}
    for i in input_list:  # The list will first iterate through all items in the list.
        if i in return_dict:  # If the item is already in return_dict then it will increase its value by 1 for each time its found within the list.
            return_dict[i] += 1
        else: 
            return_dict[i] = 1
    return return_dict

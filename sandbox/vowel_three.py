"""vowels and threes test."""


def vowels_and_threes(s: str) -> str:
    new_str: str = ""
    i: int = 0
    while i < len(s):
        v_list: list[str] = ["a", "e", "i", "o", "u"]
        if i % 3 == 0 and s[i] in v_list:
            new_str += ""
        elif i % 3 == 0:
            new_str += s[i]
        elif s[i] in v_list:
            new_str += s[i]
        i += 1
    return new_str
"""Messing with global variables."""

a: int = 6
b: int = 0
c: int = 4


def wowww(j: int) -> int:
    global a 
    wow: int = 0
    wow = a * j
    return wow


def vowel(word: str) -> dict[str, int]:
    new_vowels: dict[str, int] = {}
    i: int = 0
    vowel_list: list[str] = ["a", "e", "i", "o", "u"]
    while i < len(word):
        if word[i] in vowel_list:
            if word[i] in new_vowels:
                new_vowels[word[i]] += 1
            else:
                new_vowels[word[i]] = 1
        i += 1
    return new_vowels


"""Can't wait to drop out :D"""
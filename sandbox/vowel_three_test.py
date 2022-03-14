"""Testing :D."""


from sandbox.vowel_three import vowels_and_threes


def test_vowels_and_threes() -> None:
    p: str = "papa"
    assert vowels_and_threes(p) == "pa"
"""EX03- Wordle! For Real This Time!"""

__author__ = """730477174"""


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word_global: str = "codes"
    turns: int = 1
    while turns <= 6 and input_guess != secret_word_global:
        print(f"=== Turn {turns}/6 ===")
        if secret_word_global == input_guess and turns <= 6:
            print(f"You won in {turns}/6 turns!")
            exit()
        input_guess(len(secret_word_global))
        print(emojified(str(input_guess), secret_word_global))
        turns += 1
    if turns > 6 and input_guess != secret_word_global:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, character: str) -> bool:
    """Will return the bool 'True' or 'False' depending on if character is detected within a word."""
    assert len(character) == 1
    index: int = 0
    correct_letter_index: int = 0
    while index < len(word):
        if character != word[index]:
            index += 1
        elif character == word[index]:
            index += 1
            correct_letter_index += 1
        if correct_letter_index > 0:
            return True
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """Emojified will take the correct letters between the secret_word and guessed_word and place a green, yellow, or white emoji in its proper position within the word."""
    assert len(guessed_word) == len(secret_word)
    index: int = 0
    result_emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret_word):
        if secret_word[index] == guessed_word[index]:
            result_emoji += GREEN_BOX
            index += 1
        elif contains_char(secret_word, guessed_word[index]) is True: 
            result_emoji += YELLOW_BOX
            index += 1
        elif contains_char(secret_word, guessed_word[index]) is False:
            result_emoji += WHITE_BOX
            index += 1
    return result_emoji


"""Emojified needs to burn in a fire."""


def input_guess(expected_length: int) -> str:
    """Will prompt the user to guess a word and will return an error if it is not found."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess




    

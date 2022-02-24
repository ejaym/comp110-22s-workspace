"""EX03- Wordle! For Real This Time!"""

__author__ = """730477174"""


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word_global: str = "frizz"  # This is the variable that contains the secret word used throughout the program.
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_word_global))  # Here I am binding the length of the secret word as the argument to be used in the input_guess function so that it is easier to write later on.
        print(emojified(guess, secret_word_global))  # This statement ensures the emoji boxes are actually printed by giving emojified arguements to fit its parameters.
        if secret_word_global == guess and turns <= 6: 
            print(f"You won in {turns}/6 turns!")
            turns = 7
        if secret_word_global != guess and turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1


def contains_char(word: str, character: str) -> bool:
    """Will return the bool 'True' or 'False' depending on if character is detected within a word."""
    assert len(character) == 1
    index: int = 0
    correct_letter_index: int = 0  # This variable is curcial to returning the correct bool, basically if it's greater than 0 it will produce a True bool statement which will be used later for emojified and yellow boxes.
    while index < len(word):  
        if character != word[index]:
            index += 1
        elif character == word[index]:
            index += 1
            correct_letter_index += 1
        if correct_letter_index > 0:
            return True
    return False  # If a false is returned this is used later in emojified to print a white box.


def emojified(guessed_word: str, secret_word: str) -> str:
    """Emojified will take the matching characters between the secret_word and guessed_word and place a green, yellow, or white emoji in its proper position based on whether or not the character was found within the secret word."""
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
    return result_emoji  # By returning whatever the resulting emoji is, emojified now contains the string of emojis that corosponds to the correct characters in a word. Using the contains_char function I am then able to say if the character exists somewhere in the word (yellow box) or not at all (white box).


def input_guess(expected_length: int) -> str:
    """Will prompt the user to input a word and will return an error if the guessed word is not equal to the length of the secret word."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


if __name__ == "__main__":
    main()


    

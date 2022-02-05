"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730477174"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "cantaloupe"
guessed_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
result_emoji: str = ""  
index: int = 0

while len(guessed_word) != len(secret_word):
    guessed_word: str = input(f"That was not {len(secret_word)} letters! Try again: ")  # This took me forever to figure out becuase it kept saying "None". Forgot that I needed to actually progress the statement to move on.

while index < len(secret_word):
    if guessed_word[index] == secret_word[index]:  
        result_emoji += GREEN_BOX
    else:  # Here is the split off where the indexes don't match up, and thus where I can put a second while statement to handle the white and yellow bricks.
        wrong_place_index: int = 0
        matched_character: bool = False
        while matched_character is not True and wrong_place_index < len(secret_word):
            if guessed_word[index] == secret_word[wrong_place_index]:  # This is the line that compares words for like characters.
                matched_character = True
            wrong_place_index += 1  # Wrong place index goes up here so the next loop the next letter can be checked.
        if matched_character:
            result_emoji += YELLOW_BOX
        else:
            result_emoji += WHITE_BOX
    index += 1  # This increases the guessed word's index so that a brand new letter can be compared to a different letter in the secret word.

print(result_emoji)
if guessed_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite! Play again soon!")
"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730477174"

words: str = input("Enter a 5-character word: ")
if len(words) > 5: 
    print("Error: Word must contain 5 characters")
    exit()
if len(words) < 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) > 1:
    print("Error: Character must be a single character.")
if len(character) < 1:
    print("Error: Character must be a single character.")
instances: int = 0


print("Searching for " + character + " in " + words)
if character == words[0]:
    print(character + " found at index " + "0")
    instances = instances + 1
if character == words[1]:
    print(character + " found at index " + "1")
    instances = instances + 1
if character == words[2]:
    print(character + " found at index " + "2")
    instances = instances + 1
if character == words[3]:
    print(character + " found at  index " + "3")
    instances = instances + 1
if character == words[4]:
    print(character + " found at index " + "4")
    instances = instances + 1


if instances == 1:
    print(str(instances) + " instance of " + character + " found in " + words)
if instances == 0: 
    print("No instances of " + character + " found in " + words)
if instances > 1:
    print(str(instances) + " instances of " + character + " found in " + words)
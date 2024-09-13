"""EX02 - Chardle - Play a game similar to Wordle!"""

__author__: str = "730748249"


def input_word() -> str:
    word_choice: str = input("Enter a 5-character word: ")
    if len(word_choice) != 5:  # using two equal signs for conditional use
        # removed elif, now just using one.
        print("Error: Word must contain 5 characters.")
        exit()
    return word_choice  # return even if there is an error


def input_letter() -> str:
    letter_choice: str = input("Enter a single character: ")
    if len(letter_choice) != 1:
        print(
            "Error: Character must be a single character."
        )  # don't actually need elif here
        exit()
    return letter_choice  # return even if there is an error


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # have to turn count to str in order to concatenate


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()

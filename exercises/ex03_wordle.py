"""EX03 - Wordle - Creating a Version of Wordle"""

__author__: str = "730748249"


def input_guess(secret_word_len: int) -> str:
    """Return the guessed word after making sure it is the correct length."""
    user_guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # using f notation for ease
    index: int = len(user_guess)  # setting index here to start
    # i like to use index instead of count
    while index != secret_word_len:
        user_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        index = len(user_guess)
    return user_guess


def contains_char(secret_word: str, character: str) -> bool:
    """Searches through a string in order to find a specific character"""
    assert len(character) == 1
    index: int = 0
    letter_present: bool = False
    # def as false, so that the while loop can only change to True
    while index < len(secret_word):
        if secret_word[index] == character:
            letter_present = True
        # not using an elif because it's already false otherwise
        index += 1
    return letter_present  # only return after the while loop


def emojified(user_guess: str, secret_word: str) -> str:
    """Return emojis based on if a user guess is correct"""
    assert len(user_guess) == len(secret_word)
    index: int = 0
    emoji_output: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    while index < len(secret_word):
        if secret_word[index] == user_guess[index]:
            emoji_output = f"{emoji_output}{green_box}"
            # f syntax so I don't have to concatenate syntax
        elif contains_char(secret_word=secret_word, character=user_guess[index]):
            emoji_output = f"{emoji_output}{yellow_box}"
        else:
            emoji_output = f"{emoji_output}{white_box}"
        index = index + 1
        # increase index no matter what
    print(emoji_output)
    return emoji_output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # start at 1 for the printing
    win: bool = False
    while turn <= 6 and (not win):
        # because turn starts at 1 instead of 0, I used <= 6 instead of < 6
        print(f"=== Turn {turn}/6 ===")
        user_input: str = input_guess(secret_word_len=len(secret))
        emojified(user_guess=user_input, secret_word=secret)
        if secret == user_input:
            win = True
            break
        else:
            turn = turn + 1
            # increase the "index"
        if turn > 6 and secret != user_input:
            break
            # if they don't win, it exits the program
    if win:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

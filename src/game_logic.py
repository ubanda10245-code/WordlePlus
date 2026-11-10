"""Game rules used by the WordlePlus application."""

def evaluate_guess(guess, target):
    """Return the Wordle-style state for each letter in *guess*.

    ``correct`` marks the right letter in the right place, ``present`` marks
    a letter that occurs elsewhere in the word, and ``absent`` marks all
    other letters.  Matching correct positions first also handles repeated
    letters correctly.
    """
    states = ["absent"] * len(guess)
    remaining = list(target)

    # Identify correct letters in the correct positions
    for index, letter in enumerate(guess):
        if letter == target[index]:
            states[index] = "correct"
            remaining[index] = None

    # Identify letters that are present but in the wrong position
    for index, letter in enumerate(guess):
        if states[index] == "absent" and letter in remaining:
            states[index] = "present"
            remaining[remaining.index(letter)] = None

    return states

# If the player has guessed the target word
def check_win(guess: str, target_word: str) -> bool:
    """Return whether *guess* matches *target_word* (ignoring letter case)."""
    return guess.upper() == target_word.upper()

# If the player has used all their guesses and not found the target word.
def has_lost(guesses, target: str, maximum_guesses: int = 5) -> bool:
    """Return whether the player used every guess without finding *target*."""
    return len(guesses) >= maximum_guesses and guesses[-1][0] != target

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

    for index, letter in enumerate(guess):
        if letter == target[index]:
            states[index] = "correct"
            remaining[index] = None

    for index, letter in enumerate(guess):
        if states[index] == "absent" and letter in remaining:
            states[index] = "present"
            remaining[remaining.index(letter)] = None

    return states


def has_lost(guesses, target, maximum_guesses=5):
    """Return whether the player used every guess without finding *target*."""
    return len(guesses) >= maximum_guesses and guesses[-1][0] != target

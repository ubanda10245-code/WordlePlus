def check_win(guess, target_word):
    """
    Check if the player's guess matches the target word.
    Return True if the player wins, otherwise False.
    """
    return guess.upper() == target_word.upper()
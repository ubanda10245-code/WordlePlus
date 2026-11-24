"""Score calculation functions for WordlePlus."""

POINTS_PER_LETTER = 10
MAX_GUESSES = 5


def calculate_letter_points(states):
    """Award 10 points for each correctly placed letter."""
    correct_letters = states.count("correct")
    return correct_letters * POINTS_PER_LETTER


def calculate_win_bonus(guesses_used):
    """Award more bonus points for winning in fewer guesses."""
    remaining_guesses = MAX_GUESSES - guesses_used + 1
    return max(0, remaining_guesses) * 10

HINT_PENALTY = 20


def calculate_hint_penalty():
    """Return the point penalty for using a vowel hint."""
    return HINT_PENALTY
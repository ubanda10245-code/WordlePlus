"""Load and select words for WordlePlus."""

from pathlib import Path
import random

DICTIONARY_PATH = Path(__file__).with_name("word_dictionary.txt")

def get_words():
    """Return the usable five-letter words in the bundled dictionary."""
    with DICTIONARY_PATH.open(encoding="utf-8") as dictionary:
        return [
            word.strip().upper()
            for word in dictionary
            if len(word.strip()) == 5 and word.strip().isalpha()
        ]


def choose_word(previous_word=None):
    """Choose a target word, avoiding the previous target when possible."""
    words = get_words()
    choices = [word for word in words if word != previous_word]
    return random.choice(choices or words)

"""Load and select words for WordlePlus."""

from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent

DIFFICULTY_CONFIG = {
    "EASY": (BASE_DIR / "word_dictionary_easy.txt", 3),
    "MEDIUM": (BASE_DIR / "word_dictionary.txt", 5),
    "HARD": (BASE_DIR / "word_dictionary_hard.txt", 6),
}


def get_words(difficulty="MEDIUM"):
    """Return usable words matching the word length for *difficulty*."""
    dictionary_path, word_length = DIFFICULTY_CONFIG.get(
        difficulty.upper(), DIFFICULTY_CONFIG["MEDIUM"]
    )
    with dictionary_path.open(encoding="utf-8") as dictionary:
        return [
            word.strip().upper()
            for word in dictionary
            if len(word.strip()) == word_length and word.strip().isalpha()
        ]


def choose_word(previous_word=None, difficulty="MEDIUM"):
    """Choose a target word for *difficulty*, avoiding the previous target when possible."""
    words = get_words(difficulty)
    choices = [word for word in words if word != previous_word]
    return random.choice(choices or words)

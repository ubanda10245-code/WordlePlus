# In game_logic.py


def evaluate_guess(guess: str, target: str) -> list[str]:
  """Evaluate a 5-letter guess against the target word.

  Returns a list of 5 status strings: 'correct', 'present', or 'absent'.
  """
  states = ["absent"] * len(guess)
  remaining_target = list(target)

  # Pass 1: Identify all correct letters in correct positions (Green)
  for i, letter in enumerate(guess):
    if letter == target[i]:
      states[i] = "correct"
      remaining_target[i] = None

  # Pass 2: Identify misplaced letters (Yellow) vs absent letters (Grey)
  for i, letter in enumerate(guess):
    if states[i] == "absent" and letter in remaining_target:
      states[i] = "present"
      remaining_target[remaining_target.index(letter)] = None

  return states

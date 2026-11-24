'''This module handles all ui elements of the game.'''

import pygame

# Window dimensions
WIDTH, HEIGHT = 1280, 800

# Colors
BACKGROUND = (18, 18, 18)
FONT_COLOR = (255, 255, 255)
TILE_COLOR = (35, 35, 35)
TILE_BORDER_COLOR = (90, 90, 90)
CORRECT_COLOR = (83, 141, 78)
PRESENT_COLOR = (181, 159, 59)
ABSENT_COLOR = (58, 58, 60)
ERROR_COLOR = (220, 70, 70)

# Game board dimensions
ROWS = 5
TILE_SIZE = 64
TILE_GAP = 10

# Requirement 13: Vowel hint button
HINT_BUTTON = pygame.Rect(WIDTH // 2 - 100, 730, 200, 50)

# Difficulty selection buttons
DIFFICULTY_BUTTONS = {
    "EASY": pygame.Rect(WIDTH // 2 - 140, 300, 280, 65),
    "MEDIUM": pygame.Rect(WIDTH // 2 - 140, 395, 280, 65),
    "HARD": pygame.Rect(WIDTH // 2 - 140, 490, 280, 65),
}


def make_fonts():
    """Dictionary of font types."""
    return {
        "title": pygame.font.Font(None, 120),
        "body": pygame.font.Font(None, 40),
        "tile": pygame.font.Font(None, 64)
    }


def draw_text(screen, text, font, color, center):
    """Draws text on the screen.
    - screen (pygame.Surface): The window to draw on
    - text (str): Text to print
    - font (pygame.font.Font): Desired font type
    - color (tuple): RGB value
    - center (tuple): X and Y position
    """
    surface = font.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=center))


def draw_start_screen(screen, fonts):
    """Start screen that displays program name and prompts the user to play.
    """
    screen.fill(BACKGROUND)

    draw_text(
        screen, "WordlePlus", fonts["title"],
        FONT_COLOR, (WIDTH // 2, 220)
    )

    draw_text(
        screen, "Press Enter to play", fonts["body"],
        FONT_COLOR, (WIDTH // 2, 330)
    )


def draw_difficulty_screen(screen, fonts):
    """Display difficulty selection screen with EASY, MEDIUM, and HARD options."""
    # Clear the previous game before showing difficulty selection.
    screen.fill(BACKGROUND)
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 175))
    screen.blit(overlay, (0, 0))

    draw_text(
        screen, "Select Difficulty", fonts["title"],
        FONT_COLOR, (WIDTH // 2, 160)
    )

    draw_text(
        screen, "Choose a difficulty to begin:", fonts["body"],
        FONT_COLOR, (WIDTH // 2, 235)
    )

    button_colors = {
        "EASY": CORRECT_COLOR,
        "MEDIUM": PRESENT_COLOR,
        "HARD": ERROR_COLOR,
    }

    for label, rect in DIFFICULTY_BUTTONS.items():
        pygame.draw.rect(screen, button_colors[label], rect, border_radius=8)
        pygame.draw.rect(screen, TILE_BORDER_COLOR, rect, width=2, border_radius=8)
        draw_text(screen, label, fonts["body"], FONT_COLOR, rect.center)

    draw_text(
        screen,
        "Click a button or press E (Easy), M (Medium), or H (Hard)",
        fonts["body"],
        FONT_COLOR,
        (WIDTH // 2, 625)
    )


def get_difficulty_click(position):
    """Return 'EASY', 'MEDIUM', or 'HARD' if *position* clicks a button, else None."""
    for difficulty, rect in DIFFICULTY_BUTTONS.items():
        if rect.collidepoint(position):
            return difficulty
    return None


def draw_game_board(screen, current_guess, fonts, guesses=None, word_length=5):
    """Draws the 5x5 game board and displays typed letters.

    Args:
        screen (pygame.Surface): The game window.
        current_guess (str): Letters currently entered by the player.
        guesses (list): Submitted guesses and their evaluated letter states.
    """
    # Calculate the total board dimensions.
    board_width = word_length * TILE_SIZE + (word_length - 1) * TILE_GAP
    board_height = ROWS * TILE_SIZE + (ROWS - 1) * TILE_GAP

    # Calculate the top-left corner to center the board.
    start_x = (WIDTH - board_width) // 2
    start_y = (HEIGHT - board_height) // 2 + 50

    # Draw each tile.
    for row in range(ROWS):
        for col in range(word_length):
            x = start_x + col * (TILE_SIZE + TILE_GAP)
            y = start_y + row * (TILE_SIZE + TILE_GAP)

            tile = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

            letter = ""
            color = TILE_COLOR
            if guesses and row < len(guesses):
                word, states = guesses[row]
                letter = word[col]
                color = {
                    "correct": CORRECT_COLOR,
                    "present": PRESENT_COLOR,
                    "absent": ABSENT_COLOR
                }[states[col]]
            elif row == len(guesses or []) and col < len(current_guess):
                letter = current_guess[col]

            pygame.draw.rect(screen, color, tile)
            pygame.draw.rect(
                screen, TILE_BORDER_COLOR, tile, width=2
            )

            if letter:
                draw_text(
                    screen,
                    letter,
                    fonts["tile"],
                    FONT_COLOR,
                    (x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                )

def draw_game_placeholder(
    screen,
    fonts,
    current_guess="",
    guesses=None,
    error_message="",
    word_length=5,
    score=0,
    vowel_hint=None,
    hint_used=False
):
    """Displays the game board, instructions, and error messages."""

    screen.fill(BACKGROUND)

    draw_text(
        screen,
        f"Type a {word_length}-letter word and press Enter",
        fonts["body"],
        FONT_COLOR,
        (WIDTH // 2, 170)
    )

    draw_text(
        screen,
        f"Score: {score}",
        fonts["body"],
        (245, 205, 85),
        (WIDTH // 2, 245)
    )

    if error_message:
        draw_text(
            screen,
            error_message,
            fonts["body"],
            ERROR_COLOR,
            (WIDTH // 2, 220)
        )

    draw_game_board(screen, current_guess, fonts, guesses, word_length)

    # Requirement 13.1: Display vowel positions.
    if vowel_hint is not None:
        hint_text = "  ".join(
            letter if letter else "_" for letter in vowel_hint
        )
        draw_text(
            screen,
            hint_text,
            fonts["body"],
            PRESENT_COLOR,
            (WIDTH // 2, 680)
        )

    # Requirement 13: Display the hint button.
    button_color = ABSENT_COLOR if hint_used else CORRECT_COLOR
    pygame.draw.rect(
        screen, button_color, HINT_BUTTON, border_radius=8
    )
    pygame.draw.rect(
        screen, TILE_BORDER_COLOR, HINT_BUTTON,
        width=2, border_radius=8
    )

    button_text = "Hint Used" if hint_used else "Reveal Vowels"
    draw_text(
        screen,
        button_text,
        fonts["body"],
        FONT_COLOR,
        HINT_BUTTON.center
    )

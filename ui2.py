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

# Game board dimensions
ROWS = 5
COLS = 5
TILE_SIZE = 64
TILE_GAP = 10


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


def draw_game_board(screen, current_guess, fonts, guesses=None):
    """Draws the 5x5 game board and displays typed letters.

    Args:
        screen (pygame.Surface): The game window.
        current_guess (str): Letters currently entered by the player.
        guesses (list): Submitted guesses and their evaluated letter states.
    """
    # Calculate the total board dimensions.
    board_width = COLS * TILE_SIZE + (COLS - 1) * TILE_GAP
    board_height = ROWS * TILE_SIZE + (ROWS - 1) * TILE_GAP

    # Calculate the top-left corner to center the board.
    start_x = (WIDTH - board_width) // 2
    start_y = (HEIGHT - board_height) // 2 + 50

    # Draw each tile.
    for row in range(ROWS):
        for col in range(COLS):
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


def draw_game_placeholder(screen, fonts, current_guess="", guesses=None):
    """Displays the game board and instructions during gameplay."""
    screen.fill(BACKGROUND)

    # Requirement 6: Display the guess instructions.
    draw_text(
        screen,
        "Type a 5-letter word and press Enter",
        fonts["body"],
        FONT_COLOR,
        (WIDTH // 2, 170)
    )

    # Requirements 5 and 6.1: Display the board and typed letters.
    draw_game_board(screen, current_guess, fonts, guesses)

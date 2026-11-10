"""End-screen rendering and retry-button helpers."""

import random

import pygame

import ui

# Celebration colors
GREEN = (83, 190, 110)
YELLOW = (245, 205, 85)
PINK = (255, 120, 160)
BLUE = (100, 180, 255)
PURPLE = (180, 130, 255)
RED = (235, 90, 90)
CONFETTI_COLORS = [GREEN, YELLOW, PINK, BLUE, PURPLE, RED]


RETRY_BUTTON = pygame.Rect(ui.WIDTH // 2 - 150, 570, 300, 60)

def make_confetti(seed, count=70):
    """Return confetti pieces as (x, y, color, size) tuples.
 
    Uses its own random generator, so the pieces stay in the same place and
    the global random state (used to choose target words) is not touched.
    """
    rng = random.Random(seed)
    pieces = []
    for i in range(count):
        x = rng.randint(30, ui.WIDTH - 30)
        y = rng.randint(30, ui.HEIGHT - 30)
        color = rng.choice(CONFETTI_COLORS)
        size = rng.randint(4, 9)
        pieces.append((x, y, color, size))
    return pieces

confetti = make_confetti(seed=42)

def draw_retry_button(screen, fonts):
    """Draw the Retry button used by both end screens."""
    pygame.draw.rect(screen, GREEN, RETRY_BUTTON, border_radius=12)
    ui.draw_text(
        screen,
        "Press Enter to Retry",
        fonts["body"],
        (18, 18, 18),
        RETRY_BUTTON.center
    )

def draw_win_screen(screen, fonts):
    """Display a celebration over the already-drawn board when the player wins."""
 
    overlay = pygame.Surface((ui.WIDTH, ui.HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 175))
    screen.blit(overlay, (0, 0))
 
    # Colorful confetti
    for x, y, color, size in confetti:
        pygame.draw.rect(
            screen,
            color,
            (x, y, size, size),
            border_radius=2
        )
 
    # Main title
    ui.draw_text(
        screen,
        "YOU WIN!",
        fonts["title"],
        GREEN,
        (ui.WIDTH // 2, 220)
    )
 
    # Congratulations message
    ui.draw_text(
        screen,
        "Congratulations!",
        fonts["body"],
        ui.FONT_COLOR,
        (ui.WIDTH // 2, 330)
    )
 
    draw_retry_button(screen, fonts)
 
    return RETRY_BUTTON

def draw_lose_screen(screen, fonts, target_word):
    """Draw the lose message over the board, with the Retry button.
 
    The board must already be drawn on *screen* before this is called.
    """
    overlay = pygame.Surface((ui.WIDTH, ui.HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 175))
    screen.blit(overlay, (0, 0))

    ui.draw_text(screen, "Out of guesses", fonts["title"], ui.FONT_COLOR,
                 (ui.WIDTH // 2, 400))
    ui.draw_text(screen, "The word was " + target_word, fonts["body"],
                 ui.FONT_COLOR, (ui.WIDTH // 2, 485))
 
    draw_retry_button(screen, fonts)
 
    return RETRY_BUTTON

def is_retry_click(position):
    """Return whether *position* is inside the Retry button."""
    return RETRY_BUTTON.collidepoint(position)

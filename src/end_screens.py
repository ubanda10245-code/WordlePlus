"""Handles the win and lose screens for WordlePlus."""

import pygame
import random
import ui


# Celebration colors
GREEN = (83, 190, 110)
YELLOW = (245, 205, 85)
PINK = (255, 120, 160)
BLUE = (100, 180, 255)
PURPLE = (180, 130, 255)

CONFETTI_COLORS = [GREEN, YELLOW, PINK, BLUE, PURPLE]

# Generate confetti once so it stays in place
random.seed(42)

confetti = []

for i in range(70):
    x = random.randint(30, ui.WIDTH - 30)
    y = random.randint(30, ui.HEIGHT - 30)
    color = random.choice(CONFETTI_COLORS)
    size = random.randint(4, 9)

    confetti.append((x, y, color, size))


def draw_win_screen(screen, fonts):
    """Display a colorful celebration screen when the player wins."""

    # Dark background
    screen.fill(ui.BACKGROUND)

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

    # Retry button
    retry_button = pygame.Rect(
        ui.WIDTH // 2 - 150,
        400,
        300,
        65
    )

    pygame.draw.rect(
        screen,
        GREEN,
        retry_button,
        border_radius=12
    )

    ui.draw_text(
        screen,
        "Press Enter to Retry",
        fonts["body"],
        (18, 18, 18),
        retry_button.center
    )

    return retry_button
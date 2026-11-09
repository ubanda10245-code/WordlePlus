"""End-screen rendering and retry-button helpers."""

import pygame

import ui


RETRY_BUTTON = pygame.Rect(ui.WIDTH // 2 - 110, 570, 220, 60)


def draw_end_screen(screen, fonts, target_word, won):
    """Draw the final result and the button used to begin another game."""
    heading = "You won!" if won else "Out of guesses"
    message = "Great work!" if won else "The word was " + target_word

    overlay = pygame.Surface((ui.WIDTH, ui.HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 175))
    screen.blit(overlay, (0, 0))
    ui.draw_text(screen, heading, fonts["title"], ui.FONT_COLOR,
                 (ui.WIDTH // 2, 400))
    ui.draw_text(screen, message, fonts["body"], ui.FONT_COLOR,
                 (ui.WIDTH // 2, 485))
    pygame.draw.rect(screen, (83, 141, 78), RETRY_BUTTON, border_radius=6)
    ui.draw_text(screen, "Retry", fonts["body"], ui.FONT_COLOR,
                 RETRY_BUTTON.center)


def is_retry_click(position):
    """Return whether *position* is inside the Retry button."""
    return RETRY_BUTTON.collidepoint(position)

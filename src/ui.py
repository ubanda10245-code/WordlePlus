'''This module handles all ui elements of the game.'''

import pygame

# Window dimensions 
WIDTH, HEIGHT = 1280, 800
# Colors
BACKGROUND = (18, 18, 18)
FONT_COLOR = (255, 255, 255)


def make_fonts():
    """ Dictionary of font types
    - title (Default font, size 120px)
    - body (Default font, size 40px)
    """
    return {"title": pygame.font.Font(None, 120), 
            "body": pygame.font.Font(None, 40)}

def draw_text(screen, text, font, color, center):
    """ Draws text on the screen
    - screen (pygame.Surface): The window to draw on
    - text (str): Text to print
    - font (pygame.font.Font): Desired font type
    - color (tuple): RGB value
    - center (tuple): X and Y position
    """
    surface = font.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=center))

def draw_start_screen(screen, fonts):
    """ Start screen that displays program name and prompts the user to play.
    """
    screen.fill(BACKGROUND)
    draw_text(screen, "WordlePlus", fonts["title"],
               FONT_COLOR, (WIDTH // 2, 220))
    draw_text(screen, "Press Enter to play", fonts["body"],
               FONT_COLOR, (WIDTH // 2, 330))


# We might add the WIN and LOSE screens here instead of a different Python file.


# THIS CAN BE COPIED AND PASTED AS NEEDED TO MAKE NEW WINDOWS
def draw_game_placeholder(screen, fonts):
    """ TEMPLATE
    """
    screen.fill(BACKGROUND)
    draw_text(screen, "Placeholder", fonts["title"],
               FONT_COLOR, (WIDTH // 2, 260))
    draw_text(screen, "In progress...", fonts["body"],
               FONT_COLOR, (WIDTH // 2, 340))
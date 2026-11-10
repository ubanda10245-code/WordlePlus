import pygame
import ui
from end_screens import draw_win_screen
from game_logic import check_win

pygame.init()

screen = pygame.display.set_mode((ui.WIDTH, ui.HEIGHT))
pygame.display.set_caption("WordlePlus - Requirement 8 Test")

fonts = ui.make_fonts()

# Temporary target word for testing
target_word = "APPLE"

screen_state = "start"
current_guess = ""
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:

                # Start screen -> Playing screen
                if screen_state == "start":
                    screen_state = "playing"
                    current_guess = ""

                # Playing screen -> Check guess
                elif screen_state == "playing":

                    if len(current_guess) == 5:

                        if check_win(current_guess, target_word):
                            screen_state = "win"

                        else:
                            # Temporary behavior until guess submission is implemented
                            current_guess = ""

                # Win screen -> Restart game
                elif screen_state == "win":
                    current_guess = ""
                    screen_state = "start"

            elif screen_state == "playing":

                if event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]

                elif event.unicode.isalpha() and len(current_guess) < 5:
                    current_guess += event.unicode.upper()

    # Draw the current screen
    if screen_state == "start":
        ui.draw_start_screen(screen, fonts)

    elif screen_state == "playing":
        ui.draw_game_placeholder(screen, fonts, current_guess)

    elif screen_state == "win":
        draw_win_screen(screen, fonts)

    pygame.display.flip()

pygame.quit()
"""WordlePlus entry point. Imports all other Python files.
"""

import pygame

import end_screens
import game_logic
import input_handler
import ui
import word_manager

FPS = 60


class App:
    def __init__(self):
        """Create main window."""
        pygame.init()

        self.screen = pygame.display.set_mode((ui.WIDTH, ui.HEIGHT))
        pygame.display.set_caption("WordlePlus")

        self.clock = pygame.time.Clock()
        self.fonts = ui.make_fonts()

        self.running = True
        self.screen_state = "start"

        # Current guess entered by the player.
        self.current_guess = ""
        self.guesses = []
        self.error_message = ""
        self.target_word = word_manager.choose_word()

    def reset_game(self):
        """Start a new game with an empty board and a new target word."""
        self.target_word = word_manager.choose_word(self.target_word)
        self.current_guess = ""
        self.guesses = []
        self.error_message = ""

    def screen_transitions(self, action, value):
        """Update screen state based on user events."""

        if action == "quit":
            self.running = False

        elif self.screen_state == "start" and action == "enter":
            self.screen_state = "playing"
            self.reset_game()

        
        elif self.screen_state == "playing" and action == "letter":
            # Only allow five letters in the current guess.
            if len(self.current_guess) < 5:
                self.current_guess += value
                self.error_message = ""

        elif self.screen_state == "playing" and action == "backspace":
            self.current_guess = self.current_guess[:-1]
            self.error_message = ""

        elif self.screen_state == "playing" and action == "enter":
            if len(self.current_guess) == 5:
                self.error_message = ""

                states = game_logic.evaluate_guess(
                    self.current_guess, self.target_word
                )

                self.guesses.append((self.current_guess, states))


                if game_logic.check_win(self.current_guess, self.target_word):

                    self.screen_state = "won"
                elif game_logic.has_lost(
                    self.guesses, self.target_word
                ):
                    self.screen_state = "lost"

                self.current_guess = ""

            else:
                self.error_message = "Enter 5 letters."


        elif self.screen_state in ("won", "lost"):
            if action == "enter" or (
                    action == "click" and end_screens.is_retry_click(value)):
                self.reset_game()
                self.screen_state = "playing"

    def draw_screen(self):
        """Draw new/updated screen state."""
 
        if self.screen_state == "start":
            ui.draw_start_screen(self.screen, self.fonts)
 
        elif self.screen_state == "playing":
            ui.draw_game_placeholder(
                self.screen, self.fonts, self.current_guess, self.guesses, self.error_message
            )
 
        elif self.screen_state == "won":
            end_screens.draw_win_screen(self.screen, self.fonts)
 
        else:
            ui.draw_game_placeholder(self.screen, self.fonts, "", self.guesses)
            end_screens.draw_lose_screen(
                self.screen, self.fonts, self.target_word
            )
 
        pygame.display.flip()

    def run(self):
        """Run the main game loop until the window is closed."""

        while self.running:

            # Check for new events.
            for action, value in input_handler.get_actions():
                self.screen_transitions(action, value)

            # Draw new/updated screen.
            self.draw_screen()

            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    App().run()

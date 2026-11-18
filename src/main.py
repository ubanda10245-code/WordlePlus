"""WordlePlus entry point. Imports all other Python files.
"""

import pygame

import end_screens
import game_logic
import input_handler
import ui
import word_manager
import score_tracker

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
        self.difficulty = None

        # Current guess entered by the player.
        self.current_guess = ""
        self.guesses = []
        self.error_message = ""
        self.target_word = None
        
        self.score = 0

    def reset_game(self):
        """Start a new game with an empty board and a new target word."""
        self.target_word = word_manager.choose_word(
            self.target_word, self.difficulty or "MEDIUM"
        )
        self.current_guess = ""
        self.guesses = []
        self.error_message = ""
        self.score = 0

    def screen_transitions(self, action, value):
        """Update screen state based on user events."""

        word_length = (
            word_manager.DIFFICULTY_CONFIG[self.difficulty][1]
            if self.difficulty else 5
        )

        if action == "quit":
            self.running = False

        elif self.screen_state == "start" and action == "enter":
            self.screen_state = "difficulty"

        elif self.screen_state == "difficulty":
            selected_difficulty = None

            if action == "click":
                selected_difficulty = ui.get_difficulty_click(value)
            elif action == "letter" and value in ("E", "M", "H"):
                key_map = {"E": "EASY", "M": "MEDIUM", "H": "HARD"}
                selected_difficulty = key_map[value]

            if selected_difficulty:
                self.difficulty = selected_difficulty
                self.reset_game()
                self.screen_state = "playing"

        elif self.screen_state == "playing" and action == "letter":
            # Only allow letters of the correct length in the current guess.
            if len(self.current_guess) < word_length:
                self.current_guess += value
                self.error_message = ""

        elif self.screen_state == "playing" and action == "backspace":
            self.current_guess = self.current_guess[:-1]
            self.error_message = ""

        elif self.screen_state == "playing" and action == "enter":
            if len(self.current_guess) == word_length:
                self.error_message = ""

                states = game_logic.evaluate_guess(
                    self.current_guess, self.target_word
                )
                
                # Requirement 12.1: Award points for correctly placed letters.
                self.score += score_tracker.calculate_letter_points(states)
                print("Guess:", self.current_guess)
                print("Letter states:", states)
                print("Current score:", self.score)         

                self.guesses.append((self.current_guess, states))

                if game_logic.check_win(self.current_guess, self.target_word):
                    # Requirement 12.2: Bonus for winning in fewer guesses.
                    self.score += score_tracker.calculate_win_bonus(
                        len(self.guesses)

                     )
                    self.screen_state = "won"
                elif game_logic.has_lost(
                    self.guesses, self.target_word
                ):
                    self.screen_state = "lost"

                self.current_guess = ""

            else:
                self.error_message = f"Enter {word_length} letters."

        elif self.screen_state in ("won", "lost"):
            if action == "enter" or (
                    action == "click" and end_screens.is_retry_click(value)):
                self.screen_state = "difficulty"

    def draw_screen(self):
        """Draw new/updated screen state."""

        word_length = (
            word_manager.DIFFICULTY_CONFIG[self.difficulty][1]
            if self.difficulty else 5
        )

        if self.screen_state == "start":
            ui.draw_start_screen(self.screen, self.fonts)

        elif self.screen_state == "difficulty":
            if self.target_word is None:
                self.screen.fill(ui.BACKGROUND)
            else:
                ui.draw_game_placeholder(
                    self.screen,
                    self.fonts,
                    guesses=self.guesses,
                    word_length=word_length,
                )
            ui.draw_difficulty_screen(self.screen, self.fonts)

        elif self.screen_state == "playing":
            ui.draw_game_placeholder(
                self.screen,
                self.fonts,
                self.current_guess,
                self.guesses,
                self.error_message, 
                word_length,
                self.score
            )

        elif self.screen_state == "won":
            ui.draw_game_placeholder(
                self.screen,
                self.fonts,
                "",
                self.guesses,
                word_length=word_length,
                score=self.score
            )
            end_screens.draw_win_screen(self.screen, self.fonts, self.score)

        else:
            ui.draw_game_placeholder(
                self.screen,
                self.fonts,
                "",
                self.guesses,
                word_length=word_length,
                score=self.score
            )
            end_screens.draw_lose_screen(
                self.screen, self.fonts, self.target_word, self.score
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

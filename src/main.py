"""WordlePlus entry point. Imports all other Python files.
"""
import pygame

import input_handler
import ui

FPS = 60

class App:
    def __init__(self):
        """Create main window
        """
        pygame.init()
        self.screen = pygame.display.set_mode((ui.WIDTH, ui.HEIGHT))
        pygame.display.set_caption("WordlePlus")
        self.clock = pygame.time.Clock() # limit frame rate
        self.fonts = ui.make_fonts()
        self.running = True
        self.screen_state = "start" # Start at draw_start_screen()

    def screen_transitions(self, action):
        """Update screen state based on user events
        """
        if action == "quit":
            self.running = False
        elif self.screen_state == "start" and action == "enter":
            self.screen_state = "playing"

    def draw_screen(self):
        """Draw new/updated screen state
        """
        if self.screen_state == "start":
            ui.draw_start_screen(self.screen, self.fonts)
        else:
            ui.draw_game_placeholder(self.screen, self.fonts)
        pygame.display.flip()

    def run(self):
        """Run the main game loop until the window is closed
        """
        while self.running:
            # Check for new events
            for action, _value in input_handler.get_actions():
                self.screen_transitions(action)
            # Draw new screen
            self.draw_screen()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    App().run()
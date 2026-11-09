'''
This module handles all input events from the user.
'''

import pygame


def get_actions():
    """Get a list of actions corresponding to pygame events.

    Returns:
        List[tuple]: A list of (action, value) tuples.
    """
    actions = []

    for event in pygame.event.get():

        # Handle quit
        if event.type == pygame.QUIT:
            actions.append(("quit", None))

        # Handle keyboard input
        elif event.type == pygame.KEYDOWN:

            # Handle Enter key
            if event.key == pygame.K_RETURN:
                actions.append(("enter", None))

            # Handle Backspace key
            elif event.key == pygame.K_BACKSPACE:
                actions.append(("backspace", None))

            # Handle individual letter keys
            elif (
                len(getattr(event, "unicode", "")) == 1
                and getattr(event, "unicode", "").isascii()
                and getattr(event, "unicode", "").isalpha()
            ):
                actions.append(("letter", event.unicode.upper()))

        # Handle mouse clicks, including the Retry button.
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            actions.append(("click", event.pos))

    return actions

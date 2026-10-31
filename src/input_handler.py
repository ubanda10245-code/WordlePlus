'''
This module handles all input events from the user.
'''

import pygame

def get_actions():
    """ Get a list of actions corresponding to pygame events.
    Returns:
        List[tuple]: A list of (action, value) tuples.
    """
    actions = []
    for event in pygame.event.get():
        # Handle quit
        if event.type == pygame.QUIT:
            actions.append(("quit", None))
        # Handle enter key (pressing ENTER key down)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            actions.append(("enter", None))
    return actions
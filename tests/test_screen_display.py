import pytest
import pygame
from game import Game

@pytest.fixture
def game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return Game(screen)

def test_display_instructions(game):
    # Implement logic to test displaying a line of instructions at the top of the screen
    pass

# Generated by Nicole LeGuern
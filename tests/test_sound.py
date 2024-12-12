import pytest
from sound import Sound

@pytest.fixture
def sound():
    return Sound()

def test_play_eat_sound(sound):
    assert sound.play_eat_sound() is None

def test_play_game_over_sound(sound):
    assert sound.play_game_over_sound() is None

# Generated by Nicole LeGuern
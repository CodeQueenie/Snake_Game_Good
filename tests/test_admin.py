import pytest
from admin import AdminPanel

@pytest.fixture
def admin_panel():
    return AdminPanel()

def test_create_user_table(admin_panel):
    assert admin_panel.create_user_table() is None

def test_create_settings_table(admin_panel):
    assert admin_panel.create_settings_table() is None

def test_manage_users(admin_panel):
    assert admin_panel.manage_users() is None

def test_configure_settings(admin_panel):
    assert admin_panel.configure_settings() is None

def test_load_settings(admin_panel):
    settings = admin_panel.load_settings()
    assert isinstance(settings, dict) or settings is None

def test_save_settings(admin_panel):
    settings = {
        "game_length": 10,
        "food_size": 20,
        "game_window_width": 800,
        "game_window_height": 600
    }
    assert admin_panel.save_settings(settings) is None

# Generated by Nicole LeGuern
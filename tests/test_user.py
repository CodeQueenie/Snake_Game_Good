import pytest
from user import User

@pytest.fixture
def user():
    return User(name="test_user")

def test_create_user_table(user):
    assert user.create_user_table() is None

def test_add_user(user):
    assert user.add_user("test_user", "password") is None

def test_authenticate_user(user):
    user.add_user("test_user", "password")
    assert user.authenticate_user("test_user", "password") is True
    assert user.authenticate_user("test_user", "wrong_password") is False

# Generated by Nicole LeGuern
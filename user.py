import sqlite3
from utils import log_error

class User:
    """
    User class to manage user information.

    Attributes
    ----------
    name : str
        The name of the user.
    """

    def __init__(self, name):
        """
        Initializes the User with the given name.

        Parameters
        ----------
        name : str
            The name of the user.
        """
        self.name = name
        self.conn = sqlite3.connect("database/leaderboard.db")
        self.create_user_table()

    def create_user_table(self):
        """
        Creates the user table if it does not exist.
        """
        try:
            with self.conn:
                self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
                """)
        except Exception as e:
            log_error("create_user_table", str(e))

    def add_user(self, username, password):
        """
        Adds a new user to the database.

        Parameters
        ----------
        username : str
            The username of the new user.
        password : str
            The password of the new user.
        """
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO users (username, password)
                    VALUES (?, ?)
                """, (username, password))
        except Exception as e:
            log_error("add_user", str(e))

    def update_user(self, username, new_password):
        """
        Updates the password of an existing user.

        Parameters
        ----------
        username : str
            The username of the user.
        new_password : str
            The new password of the user.
        """
        try:
            with self.conn:
                self.conn.execute("""
                    UPDATE users
                    SET password = ?
                    WHERE username = ?
                """, (new_password, username))
        except Exception as e:
            log_error("update_user", str(e))

    def delete_user(self, username):
        """
        Deletes a user from the database.

        Parameters
        ----------
        username : str
            The username of the user to delete.
        """
        try:
            with self.conn:
                self.conn.execute("""
                    DELETE FROM users
                    WHERE username = ?
                """, (username,))
        except Exception as e:
            log_error("delete_user", str(e))

    def authenticate_user(self, username, password):
        """
        Authenticates a user by checking the username and password.

        Parameters
        ----------
        username : str
            The username of the user.
        password : str
            The password of the user.

        Returns
        -------
        bool
            True if the user is authenticated, False otherwise.
        """
        try:
            cursor = self.conn.execute("""
                SELECT * FROM users
                WHERE username = ? AND password = ?
            """, (username, password))
            return cursor.fetchone() is not None
        except Exception as e:
            log_error("authenticate_user", str(e))
            return False

# Generated by Nicole LeGuern
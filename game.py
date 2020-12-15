# pylint: disable=too-few-public-methods
"""
Let's play to the longest word
"""
import random
import string

class Game:
    """
    This is the main class for the longest word game
    """
    def __init__(self):
        """
        initialize a new game with 9 random letters
        """
        self.grid = random.choices(string.ascii_uppercase,k=9)

    def is_valid(self, word):
        """
        checks if a word is valid for this game
        """
        available_chars = list(self.grid)
        for char in word:
            try :
                available_chars.remove(char)

            except ValueError:
                return False
        return True

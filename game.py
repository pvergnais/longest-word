# pylint: disable=too-few-public-methods
"""
Let's play to the longest word
"""
import random
import string
import requests

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
        if not word:
            return False

        available_chars = list(self.grid)
        for char in word:
            try :
                available_chars.remove(char)

            except ValueError:
                return False
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        #print(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        #print (f'{json_response}')
        return json_response['found']

import unittest
from unittest.mock import patch

import hangman


class TestHangman(unittest.TestCase):

    def test_game_over(self):
        self.assertEqual(hangman.game_over(6, 'word', set('word')), True)
        self.assertEqual(hangman.game_over(6, 'word', set('wor')), True)
        self.assertEqual(hangman.game_over(5, 'word', set('word')), True)
        self.assertEqual(hangman.game_over(5, 'word', set('wor')), False)

    def test_join_guessed_letters(self):
        self.assertEqual(hangman.join_guessed_letters(set('word')), 'd o r w')
        self.assertEqual(hangman.join_guessed_letters(set('wor')), 'o r w')

    def test_build_guessed_word(self):
        self.assertEqual(hangman.build_guessed_word('word', set('word')), 'w o r d')
        self.assertEqual(hangman.build_guessed_word('word', set('wor')), 'w o r _')

    def test_validate_guess(self):
        self.assertEqual(hangman.validate_guess('a', set('word')), True)
        self.assertEqual(hangman.validate_guess('w', set('word')), False)
        self.assertEqual(hangman.validate_guess('word', set('word')), False)

    @patch('builtins.input', return_value='a')
    def test_get_player_input(self, input):
        self.assertEqual(hangman.get_player_input(set('word')), 'a')

    @patch('builtins.open', return_value=['word'])
    def test_select_word(self, open):
        self.assertEqual(hangman.select_word(), 'word')

if __name__ == "__main__":
    unittest.main()

import tkinter as tk
import unittest
from unittest.mock import patch

from GUIhangman import HangmanGUI


class TestHangmanGUI(unittest.TestCase):
    def setUp(self):
        self.gui = HangmanGUI()

    def test_update_display(self):
        self.gui.guessed_letters = set('word')
        self.gui.wrong_guesses = 2
        self.gui.update_display()
        self.assertEqual(self.gui.guessed_letters_label.cget("text"), 'd o r w')
        self.assertEqual(self.gui.hangman_label.cget("text"), '  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========')

    @patch('tkinter.messagebox.showerror')
    def test_handle_user_input_invalid(self, mock_showerror):
        self.gui.guess_entry.insert(0, 'word')
        self.gui.handle_user_input()
        mock_showerror.assert_called_once_with("Invalid guess", "Please enter a single, unguessed lowercase letter.")

    @patch('tkinter.messagebox.showerror')
    def test_handle_user_input_valid(self, mock_showerror):
        self.gui.guess_entry.insert(0, 'w')
        self.gui.handle_user_input()
        self.assertIn('w', self.gui.guessed_letters)
        mock_showerror.assert_not_called()

    @patch('hangman.select_word', return_value='word')
    def test_start_new_game(self, mock_select_word):
        self.gui.start_new_game()
        self.assertEqual(self.gui.target_word, 'word')
        self.assertEqual(self.gui.guessed_letters, set())
        self.assertEqual(self.gui.wrong_guesses, 0)

if __name__ == "__main__":
    unittest.main()

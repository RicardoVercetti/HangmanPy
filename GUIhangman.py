import tkinter as tk
import tkinter.messagebox as messagebox

from hangman import (build_guessed_word, game_over, join_guessed_letters,
                     select_word, validate_guess)
from raw_strings import draw_hanged_man


class HangmanGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.pack()
        self.guess_button = tk.Button(self.window, text="Guess", command=self.handle_user_input)
        self.guess_button.pack()
        self.new_game_button = tk.Button(self.window, text="New Game", command=self.start_new_game)
        self.new_game_button.pack()
        self.guessed_letters_label = tk.Label(self.window, text="")
        self.guessed_letters_label.pack()
        self.hangman_label = tk.Label(self.window, text="")
        self.hangman_label.pack()
        self.start_new_game()

    def update_display(self):
        self.guessed_letters_label.config(text=join_guessed_letters(self.guessed_letters))
        self.hangman_label.config(text=draw_hanged_man(self.wrong_guesses))

    def handle_user_input(self):
        guess = self.guess_entry.get().lower()
        if validate_guess(guess, self.guessed_letters):
            self.guessed_letters.add(guess)
            if guess not in self.target_word:
                self.wrong_guesses += 1
            if game_over(self.wrong_guesses, self.target_word, self.guessed_letters):
                self.guess_button.config(state="disabled")
        else:
            tk.messagebox.showerror("Invalid guess", "Please enter a single, unguessed lowercase letter.")
        self.update_display()

    def start_new_game(self):
        self.target_word = select_word()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.guess_button.config(state="normal")
        self.update_display()

if __name__ == "__main__":
    gui = HangmanGUI()
    gui.window.mainloop()

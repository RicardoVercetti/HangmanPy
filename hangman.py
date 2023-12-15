# hangman.py

from random import choice
from raw_strings import draw_hanged_man
import string

MAX_WRONG_GUESSES = 6

# either ran out of guesses or guessed correctly
def game_over(wrong_guesses: int, target_word: str, guessed_letters: set) -> bool:
    if(wrong_guesses == MAX_WRONG_GUESSES):
        return True
    if(set(target_word) <= guessed_letters):
        return True
    return False

#return (
    #     guesses_taken == MAX_INCORRECT_GUESSES
    #     or set(target_word) <= letters_guessed
    # )
#

def join_guessed_letters(guessed_letters: set) -> str:
    return " ".join(sorted(guessed_letters))

# guessed
def build_guessed_word(target_word: str, guessed_letters: set) -> str:
    letters = []
    for letter in target_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    return " ".join(letters)

def validate_guess(player_input : str, guessed_letters: set) -> bool:
    return(len(player_input) == 1 and player_input in string.ascii_lowercase and player_input not in guessed_letters)

def get_player_input(guessed_letters: set) -> str:
    while True:
        player_input = input("Guess a letter : ").lower()
        if validate_guess(player_input, guessed_letters):
            return player_input
        else:
            print("Invalid input!")

def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
        word = choice(word_list).strip()
        return word

        # print(word)
        # print(type(word_list))
        # print("The choice :",word)


if __name__ == "__main__":
    # initial setup

    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Hangman!")

    # game loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is : {guessed_word}")
        print(f"Current guessed letters : {join_guessed_letters(guessed_letters)}")

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")

        else:
            print("Sorry, it's not there :(")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # game over
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_WRONG_GUESSES:
        print("You've lost!")
    else:
        print("Congrats! You've won!")

    print(f"Your word was {target_word}")







### PTR

# files             -   https://realpython.com/working-with-files-in-python/
# with statement    -   https://realpython.com/python-with-statement/
# input()           -   https://realpython.com/python-input-output/
# function          -   https://realpython.com/defining-your-own-python-function/
# strings           -   https://realpython.com/python-strings/
# lists             -   https://realpython.com/python-list/
# sets              -   https://realpython.com/python-sets/
# Iterable          -   

# next steps

# Wordle clone      -   https://realpython.com/python-wordle-clone/
# Quiz              -   https://realpython.com/python-quiz-application/
# dice rolling      -   https://realpython.com/python-dice-roll/
# weather CLI       -   https://realpython.com/build-a-python-weather-app-cli/
# Dir generation    -   https://realpython.com/directory-tree-generator-python/


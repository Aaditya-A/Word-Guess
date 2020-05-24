"""
File: word_guess.py
-------------------
Python Program To Illustrate Word Guess Game.
"""

import random
from simpleimage import SimpleImage

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with
YOU_LOSE_IMAGE = 'images/You Lose!.jpg'
YOU_WON_IMAGE = 'images/You Won!.jpg'

def play_game(secret_word):
    unguessed_word = ''
    for _ in range(len(secret_word)):  # initialise the secret word as blanks.
        unguessed_word += "-"

    guesses_remaining = INITIAL_GUESSES

    while True:

        print("The word now looks like this: ", unguessed_word)
        print("You have " + str(guesses_remaining) + " guesses left")
        guess = input("Type a single letter here, then press enter: ")

        # makes sure user enter only a single character.
        if len(guess) > 1:
            print("Guess should only be a single character.")
            print()                                               # prints a blank line
            continue                                              # goes back to  start of loop

        guess = guess.upper()        # accepts both lower and upper case as input.

        if guess in secret_word:     # condition when guess in correct.
            print("That guess is correct.")

            unguessed_word = update_unguessed_word(unguessed_word, guess, secret_word)

            # when user guesses all letters in secret word.
            if unguessed_word == secret_word:
                print("Congratulations, the word is: ", secret_word)
                show_winning_image()
                break

        # condition if user guess fails.
        else:
            print("There are no " + str(guess) + "'s in the word")
            guesses_remaining -= 1

            # user runs out of tries.
            if guesses_remaining == 0:
                print("Sorry, you lost. The secret word was: ", secret_word)
                show_losing_image()
                break


        print()         # makes looks nicer in terminal.

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    '''
    >>> get_word()
    '''
    word_list = []
    for line in open(LEXICON_FILE):         # Open file to read
        line = line.strip()                 # Remove newline
        word_list += line.split()           # create list of words

    j = random.randint(0, len(word_list) - 1)   # choose random integers.

    return word_list[j]                     # returns word according to index random passed


def update_unguessed_word(unguessed_word, guess, secret_word):
    # following two loops i.e., 'for' and 'if' makes sure to print all repeated guess letter.
    for y in range(len(secret_word)):

        if guess == secret_word[y]:
            # updates the guess value in unguessed word.(If not understood see the equivalent function in last comment)
            new_unguessed_word = unguessed_word[:y] + guess + unguessed_word[y + 1:]

            # updates unguessed word for forthcoming repeated operations.
            unguessed_word = new_unguessed_word

    return unguessed_word

def show_losing_image():
    image = SimpleImage(YOU_LOSE_IMAGE)
    image.show()

def show_winning_image():
    image = SimpleImage(YOU_WON_IMAGE)
    image.show()

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """

    secret_word = get_word()
    play_game(secret_word)

    """
    Equivalent To: new_unguessed_word = unguessed_word[:y] + guess + unguessed_word[y + 1:]
    for i in range(y):
        new_unguessed_word += unguessed_word[i]

    new_unguessed_word += guess

    for i in range(y+1, len(secret_word)):
        new_unguessed_word += unguessed_word[i]
    """
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

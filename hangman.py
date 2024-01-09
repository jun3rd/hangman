# hangman.py

import random
from words_for_hangman import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    # below used for debugging:
    # print(f"word: {word}")
    word_letters = set(word)
    # below used for debugging:
    # print(word_letters)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = len(word_letters)

    while len(word_letters) > 0 and lives > 0:
        print(f"\n{lives} lives left. You guessed:", " ".join(used_letters))

        # current guess status
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"word: ", " ".join(word_list))
        user_letter = input("guess? ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                # below used for debugging:
                # print(f"{user_letter} NOT in {word}")
                print(f"{user_letter} - wrong!")
        elif user_letter in used_letters:
            print("already used")
        else:
            print("invalid")
    if lives == 0:
        print(f"Sorry, your word was: {word}")
    else:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"word: ", " ".join(word_list))
        print(f"You win!")

if __name__ == "__main__":
    hangman()


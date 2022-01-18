"""
create a words file and read it
"""
from string import ascii_lowercase
import random
from collections import defaultdict

def return_new_word():
    words_processed_count = 0
    curr_word = None
    with open("textfile.txt","r") as f:
        for line in f:
            line = line.strip().lower()
            words_processed_count += 1
            if random.randint(1, words_processed_count) == 1:
                curr_word = line
    return curr_word

def get_display_word(word, idxs):
    displayed_word = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip() 

def get_rating(guess_counter):
    print(guess_counter)
    if guess_counter >= 5:
        return "Elite"
    elif guess_counter < 5 and guess_counter > 2:
        return "Good"
    else:
        return "Average"

def play_game():
    actual_word = return_new_word()
    length_of_word = len(actual_word)
    length_of_word_count = length_of_word
    print(actual_word)
    idxs = [letter not in ascii_lowercase for letter in actual_word]
    print("You have a {0} letter word to guess in 11 attempts.\n".format(length_of_word))
    guess_counter = 11
    while guess_counter > 0:
        guess = input("Take your guess:-")
        print(guess_counter)
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input, you have lost one guess, please be more careful.\n")
            guess_counter = guess_counter - 1 
            print("Attempts remaining {0}".format(guess_counter))
        else:
            if guess in actual_word:
                for i in range(len(actual_word)):
                    if actual_word[i] == guess:
                        idxs[i] = True
                print('Word: {0}'.format(get_display_word(actual_word, idxs)))
                length_of_word_count -= 1 
                if length_of_word_count == 0:
                    print("Hurray!!! You guessed right, the word is '{0}'".format(actual_word.upper()))
                    print(guess_counter)
                    print("Your rating for the try is {0}".format(get_rating(guess_counter)))
                    guess_counter = 0
                    break
            else:
                guess_counter = guess_counter - 1 
                print("Miss, remaining guesses {0}".format(guess_counter))
    else:
        print("Sorry, you seem ot have trouble understanding English.\n")
    if guess_counter == 0 or length_of_word_count == 0:
        try_again = input('Would you like to try again? [y/Y] ')
        return try_again.lower() == 'y'
        

if __name__ == "__main__":
    while play_game():
        print()
    

    

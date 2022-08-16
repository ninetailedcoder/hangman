import random
import string
from words import words

def hangman():
    word = random.choice(words) #randomly chooses something from the list
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() #what the user had guessed

    #getting user input
    while len(word_letters) > 0:
        #letter used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter= input('Guess a letter:').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please guess again !')
        else:
            print('pleae use a valid character.')
    print(f'congrats you got the word {word}! ')
    # gets here when len(word_letters) less than 0

print(hangman())
